
          function addThese(a,b)
            {
                var c = a + b 
                return c 
            }

            function subtractThese(a,b)
            {
                var c = a - b 
                return c 
            }

            function multiplyThese(a,b)
            {
                var c = a* b
                return c 
            }

            window.onload = function()
            {
                var x = 215 
                var y = 115.5
                var sum = addThese(x,y); 
                document.getElementById('result').innerHTML = sum 
                document.getElementById('result').innerHTML += "</br>" + 
                multiplyThese(x,y)

                document.getElementById('result').innerHTML += "</br>" + 
                subtractThese(100,50)
            }