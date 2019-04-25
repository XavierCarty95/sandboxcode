<!DOCTYPE html> 
 <html> 
     <head> 
         <title>
             Functions 
         </title>
         <script>
         function greeting(){
             var resultDiv = document.getElementById("results")
             resultDiv.innerHTML = "<h1> Greeting! </h1>"
         }
         
         window.onload = function()
         {
             greeting()
             document.getElementById('btnGreet').addEventListener('click' , greeting)
         }
         </script>
     </head>
     <body>
         <div id= "results"></div>
         <button id = "btnGreet">Greet Me!</button> 

     </body>
     </html>