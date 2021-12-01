import json
import platform
import time
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import getpass

browser_name = ''
file_name = ''
question_file_list = []
section_file_list = []
questions_data = ''
sections_data = ''
data_store_dict = {}
workflow_ids = ''
region = ''


def wf_id_data(wf_ids, reg):
    global workflow_ids, region
    workflow_ids = wf_ids
    workflow_ids = workflow_ids.split(',')
    region = reg
    browser = default_browser()
    driver = path(browser)
    data_dict = web_manipulation(driver)
    from . import parser_main
    parser_main.web_automated_data(data_dict, workflow_ids)
    return "Done"


def default_browser():
    osPlatform = platform.system()

    if osPlatform == 'Windows':
        try:
            with OpenKey(HKEY_CURRENT_USER,
                         r'SOFTWARE\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice') as regkey:
                browser_choice = QueryValueEx(regkey, 'ProgId')[0]
                return browser_choice

        except Exception as n:
            print('Failed to look up default browser in system registry. Using fallback value.', n)


def path(browser_string):
    browser_string = 'Firefox'
    if browser_string.startswith('Chrome') is True:
        options = webdriver.ChromeOptions()
        PATH = "chromedriver.exe"
        options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
        # driver = webdriver.Chrome(executable_path=PATH)

    if browser_string.startswith('Firefox') is True:
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        PATH = "geckodriver.exe"
        driver = webdriver.Firefox(options=options, executable_path=PATH)

    return driver


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)


def web_manipulation(driver):
    global questions_data, sections_data, workflow_ids, data_store_dict, first_section, region, browser_name
    try:
        global question_file_list, section_file_list
        if region == "NA":
            driver.get("https://albacore-na.aka.amazon.com/gwf/get")
        if region == "EU":
            driver.get("https://albacore-eu.aka.amazon.com/gwf/get")
        if region == "FE":
            driver.get("https://albacore-fe.aka.amazon.com/gwf/get")
        if browser_name.startswith('Chrome') is True:
            try:
                driver.find_element_by_xpath('//*[@id="details-button"]').click()
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
            except:
                print("Issue in try-except for browser name")

        time.sleep(25)
        for workflow_id in workflow_ids:
            file_name_questions = "questions_" + workflow_id + ".txt"
            file_name_sections = "sections_" + workflow_id + ".txt"
            search_wfid = driver.find_element_by_id('gwf_id')
            search_wfid.send_keys(workflow_id)
            search_wfid.send_keys(Keys.RETURN)
            time.sleep(7)
            section_list = []

            try:
                select = Select(driver.find_element_by_xpath('//*[@id="start-section-select"]/select'))
                first_section = str(select.first_selected_option.get_attribute("value"))
                wait_section = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'sections-raw')))

            except Exception as a:
                print("Wait error on element: ", a)
                status = "Data not found"
                driver.quit()
                return status
            data_store_dict[workflow_id] = first_section
            sections = driver.find_element_by_id('sections-raw').get_attribute('value')
            sections_data = sections
            question_group_link = driver.find_element_by_link_text('Question Groups')
            workflow_section = "sections_" + workflow_id
            data_store_dict[workflow_section] = sections_data
            section_file_list.append(file_name_sections)
            question_group_link.click()
            try:
                wait_question = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'question-groups-raw')))
            except Exception as i:
                print("Error on question groups: ", i)

            questions = driver.find_element_by_id('question-groups-raw').get_attribute('value')
            questions_data = questions
            workflow_question = "questions_" + workflow_id
            data_store_dict[workflow_question] = questions_data
            question_file_list.append(file_name_questions)
            driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul/li[4]/a").click()
            time.sleep(3)
    except Exception as e:
        print("An error occurred: ", e)
    return data_store_dict
    

# browser = default_browser()
# driver = path('Firefox')
# data_dict = web_manipulation(driver)
#
# web_automated_data(data_dict, workflow_ids)

