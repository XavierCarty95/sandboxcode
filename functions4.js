
             var btnPress;
             window.onload = function(){

                alert("window.onload!")
                btnPress = document.getElementById('myButton')
                btnPress.onmouseover = function()
                {
                    alert("Thanks for pressing me")
                }
             }
          
     