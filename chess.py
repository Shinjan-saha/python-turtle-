import turtle
r= turtle.Screen()
tip=turtle.Turtle()
def draw():
    for i in range(4):
        tip.forward(30)
        tip.left(90)
    tip.forward(30)
if __name__=="__main__":
    r.setup(600,600) 
    tip.speed(100)
    for j in range(8):
        tip.up()
        tip.setpos(0,30*j)
        tip.down()
        for i in range(8):
            if(i+j)%2==0:
                col="black"
            else:
                col="white"
            tip.fillcolor(col)
            tip.begin_fill()
            draw()
            tip.end_fill()

    tip.hideturtle() 