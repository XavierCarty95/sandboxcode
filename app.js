
var http = new XMLHttpRequest()

window.onload = function() {

document.getElementById("load").addEventListener("click", searchDataBase)

}
function searchDataBase(){
    
    var url = "https://jsonplaceholder.typicode.com/posts"
    http.open("GET" , url , true )
    http.onreadystatechange = trustProcess
    // console.log(http.responseText)
    http.send()
    
    
}

function trustProcess(){
    var out = "<ul>"
    var data = http.responseText
    var disdata = data.length
    console.log(disdata)
    if (http.readyState == 4 && http.status == 200) {
        
    
       
        for(var i = 0; i < data[i].length; i++){
            document.getElementById("content").innerHTML = data
            out += "<li>" + data[i] + "</li>"
            
        };
    out += "</ul>"
    }
    
}

function preven(e){
    e.preventDefault()
}

