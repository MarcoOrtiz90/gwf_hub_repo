const new_auto_question = document.getElementById("new-q-id")
new_auto_question.addEventListener('click', ((event)=>{
    console.log("entered function")
    if(event){
        event.preventDefault()
    }

    const formCopyTarget = document.getElementById('form-generator')
    const emptyFormEle = document.getElementById('q-id-1').cloneNode(true)
    list = formCopyTarget.getElementsByTagName('li')
    currentlistLength = list.length + 1 
    emptyFormEle.setAttribute('id', `q-id-${currentlistLength}`)
    formCopyTarget.append(emptyFormEle)

}))