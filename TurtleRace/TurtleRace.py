import turtle
from random import randint
from time import sleep

s=turtle.getscreen()
turtle.bgcolor('pink')
turtle.title('Turtle Race')
#objects
dic={'TurtleOne':randint(200,400),'TurtleTwo':randint(200,400),'TurtleThree':randint(200,400),'TurtleFour':randint(200,400)}

TurtleOne=turtle.Turtle()
TurtleOne.shape('turtle')
TurtleOne.color('yellow')

TurtleTwo=turtle.Turtle()
TurtleTwo.shape('turtle')
TurtleTwo.color('red')

TurtleThree=turtle.Turtle()
TurtleThree.shape('turtle')
TurtleThree.color('blue')

TurtleFour=turtle.Turtle()
TurtleFour.shape('turtle')
TurtleFour.color('green')
#placement
TurtleTwo.backward(20)
TurtleThree.forward(20)
TurtleFour.forward(40)
#race

TurtleOne.left(90)
TurtleOne.forward((dic.get('TurtleOne')))


TurtleTwo.left(90)
TurtleTwo.forward((dic.get('TurtleTwo')))


TurtleThree.left(90)
TurtleThree.forward((dic.get('TurtleThree')))


TurtleFour.left(90)
TurtleFour.forward((dic.get('TurtleFour')))

#winner
for turtles , speed in dic.items():
    if speed==max(dic.values()):
        winner = turtles

s.clear()
s.bgcolor('pink')
style=('Courier',30,'italic')
turtle.write(f'Winner is {winner}',font=style,align='center')
sleep(4)
