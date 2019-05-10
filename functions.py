
def add_it(x , y = 10):
    return x + y
    
result = add_it(2 , 15)
print(result)

x = 1
y = 2 
z = 3

def f():
    print(x)
    print(y)
    print(z)
    """
    Returs x + y. 
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    
f()

x = 100
def f():
    global x 
    x += 1  
    print(x)

f()




https://www.tutorialspoint.com/python/standard_exceptions.html
