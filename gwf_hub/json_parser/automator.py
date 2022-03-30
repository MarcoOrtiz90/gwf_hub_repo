import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

i = 1

while i > 0:
    # driver_path = 'Drivers/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver1 = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver2 = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    driver1.get('https://app.sli.do/event/joi8KAF2PpaX4EJVTxiYbF/live/polls')
    driver2.get('https://app.sli.do/event/joi8KAF2PpaX4EJVTxiYbF/live/polls')


    time.sleep(6)
    radio_to_select1 = driver1.find_element(By.XPATH, '//*[@id="live-tabpanel-polls"]/div/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label[5]/span[2]')
    radio_to_select2 = driver2.find_element(By.XPATH, '//*[@id="live-tabpanel-polls"]/div/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label[5]/span[2]')

    select_radio1 = radio_to_select1.click()
    select_radio2 = radio_to_select2.click()

    send_button1 = driver1.find_element(By.XPATH, '//*[@id="live-tabpanel-polls"]/div/div/div[2]/form/div[2]/div/button')
    send_button2 = driver2.find_element(By.XPATH, '//*[@id="live-tabpanel-polls"]/div/div/div[2]/form/div[2]/div/button')
    send_button1.click()
    send_button2.click()

    time.sleep(4)
    i += 2
    driver1.quit()
    driver2.quit()

    print("Votes this session : ", i)
