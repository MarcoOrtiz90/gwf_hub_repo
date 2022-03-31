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
    if(id == 'autoAnswer'){
        let textarea = document.getElementById('template')
        textarea.select();
        document.execCommand('copy')
        alert("Template Copied to Clipboard")
    }else{
        let textarea = document.getElementById('bpmnResult')
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

// $('#parse').click(()=>{
//     console.log("clicked")
//     $.ajax({
//         url: '',
//         type: 'get',
//         data: {
//             button_text: $(this).text()
//         },
//         success: ((response)=>{
//             $('parser-progress').width("50px")
//         })
//     })
// });

$('#parse').click(function(){
    $.ajax({
        url:'',
        type: 'get',
        data: {
            button_request: $(this).text()
        },
        success: function(response){
            $('#parser-progress').width('50%')
        }
    })
})

// let parse_status = setTimeout(()=>{
//     $.ajax({
//         url: '',
//         type: 'get',
//         data: {
//             process: 'process-request'
//         },
//         success:
//     })
// },5000);



