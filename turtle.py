import turtle 
import random 


turtles = list()

def setup(): 
    global turtles 
    startline = -480
    screen =  turtle.Screen()
    screen.setup(1290,720)
    screen.bgpic('pavement.gif')
    
    
    turtle_ycor = [-40, -20, 0, 20, 0]
    turtle.color = ['blue','red', 'purple', 'brown' , 'green']
    
    for i in range(0, len(turtle_ycor)): 
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)
        
def race():
    global turtles 
    winner = False
    finishline = 500
    
    while not winner: 
        for current_turtle in turtle.xcor():
            move = random.randint(0,2)
            current_turtle.forward(move)
            
            xcor = current_turtle.xcor()
            if(xcor >= finishline):
                winner = True
                winner.color = current_turtle.color()
                print('The winner is' , winner_color[0])
        

setup()
turtle.mainloop()
        



