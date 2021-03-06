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


function copyToClipboard(id){
    let textarea = ''
    if(id == 'autoAnswer'){
        textarea = document.getElementById('template')
        textarea.select();
        document.execCommand('copy')
        alert("Template Copied to Clipboard")
    }else if (id == 'extractor'){
        textarea = document.getElementById('bpmnResult')
        textarea.select();
        document.execCommand('copy')
        alert("BPMN Code Copied to Clipboard")
    }
    
}


function removeID(event){
    if(event){
        event.preventDefault()
    }
    
    const formCopyTarget = document.getElementById('form-generator')
    console.log(formCopyTarget)
    ids_length = formCopyTarget.getElementsByTagName("li").length
    console.log(ids_length)
    if (ids_length > 1) {
        console.log("entered if")
        let removeItm = document.getElementById(`q-id-${ids_length}`)
        console.log(removeItm)
        console.log(formCopyTarget)
        formCopyTarget.removeChild(removeItm)
    } else {
        alert("No more IDs to remove")
    }
}

