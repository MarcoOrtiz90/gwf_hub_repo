function requestIDs(event){
    if (event){
        event.preventDefault()
    }
    const formCopyTarget = document.getElementById('form-generator')
    const emptyFormEle = document.getElementById('q-id-1').cloneNode(true)
    list = formCopyTarget.getElementsByTagName('li')
    currentlistLength = list.length + 1 
    emptyFormEle.setAttribute('id', `q-id-${currentlistLength}`)
    formCopyTarget.append(emptyFormEle)
}

function removeID(event){
    if(event){
        event.preventDefault()
    }
    
    const formCopyTarget = document.getElementById('form-generator')
    ids_length = $("#form-generator").children().length
    if (ids_length > 1) {
        let removeItm = document.getElementById(`q-id-${ids_length}`)
        console.log(formCopyTarget)
        formCopyTarget.removeChild(removeItm)
    } else {
        alert("No more IDs to remove")
    }

}

