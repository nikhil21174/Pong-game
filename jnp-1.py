import mysql.connector
import turtle
from datetime import date,datetime

date=date.today()                           #time and date
time=datetime.now()
joining_time=time.strftime("%H:%M:%S")

name1=input("Enter the name of first player= ")    #name of players
name2=input("Enter the name of second player= ")
name1=name1.capitalize()
name2=name2.capitalize()
while True:
    n=int(input("Enter the score limit= "))
    if n>0:
        break

z = turtle.Screen()       #screen
z.title("Pong game")

z.setup(width=800,height=600)

a = turtle.Turtle()
a.shape("square")
a.shapesize(stretch_wid=150,stretch_len=100)      #play field
a.color("green")
a.penup()

#boundary
s = turtle.Turtle()
s.penup()
s.goto(-400,-300)
s.pendown()
s.forward(800)
s.left(90)
s.forward(600)
s.left(90)
s.forward(800)
s.left(90)
s.forward(600)
s.hideturtle()


#football ground 
cir=turtle.Turtle()
cir.color("white")
cir.penup()
cir.goto(0,300)
cir.pendown()
cir.right(90)
cir.forward(600)
cir.penup()
cir.goto(-80,0)
cir.pendown()
cir.circle(80)
cir.hideturtle()


#post
g = turtle.Turtle()
g.shape("square")
g.penup()
g.goto(-400,200)

d = turtle.Turtle()
d.shape("square")
d.penup()
d.goto(-400,-200)

x = turtle.Turtle()
x.shape("square")
x.penup()
x.goto(400,-200)

y = turtle.Turtle()
y.shape("square")
y.penup()
y.goto(400,200)


D=turtle.Turtle()
D.color("white")
D.penup()
D.goto(-400,200)
D.pendown()
D.forward(100)
D.right(90)
D.forward(400)
D.right(90)
D.forward(100)
D.penup()


D.goto(400,200)
D.pendown()
D.forward(100)
D.left(90)
D.forward(400)
D.left(90)
D.forward(100)
D.penup()
D.hideturtle()


score_a=0   
score_b=0   

f = turtle.Turtle()     #paddle 1
f.speed(0)
f.shape("square",)
f.shapesize(stretch_wid=5,stretch_len=1)
f.color("blue")
f.penup()
f.goto(-350,0)
def move() :
    y = f.ycor()
    y +=100
    f.sety(y)
def move1() :
    y = f.ycor() 
    y -=100
    f.sety(y)

z.listen()
z.onkey(move,"w")
z.onkey(move1,"s")

a = turtle.Turtle()   #paddle 2
a.speed(0)
a.shape("square",)
a.shapesize(stretch_wid=5,stretch_len=1)
a.color("blue")
a.penup()
a.goto(350,0)
def move3() :
    y = a.ycor()
    y +=100
    a.sety(y)
def move4() :
    y = a.ycor()
    y -=100
    a.sety(y)

z.onkey(move3,"i")
z.onkey(move4,"k")

q = turtle.Turtle()    #ball
q.speed(3)
q.shape("circle")
q.color("blue")
q.penup()
q.goto(0,0) 
q.dx = 5
q.dy = 5

#score board
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write((name1,":0                             ",name2,":0"), align="center",font=(20))


run=True
while run :
       
    q.setx(q.xcor() + q.dx)
    q.sety(q.ycor() + q.dy)
 
    if q.xcor() > 400 and (q.ycor() > -200 and q.ycor() < 200) :
        
        q.setx(400)
        q.goto(0,0)
        q.dx *= -1 
        score_a += 1
        pen.clear()
        pen.write("player1: {}                         player2: {}".format(score_a,score_b),align="center",font=(20))
        
    elif q.xcor() < -400 and (q.ycor() > -200 and q.ycor() < 200):      #keepinhg ball in the boundary
         
         q.setx(-400)
         q.goto(0,0)     
         q.dx *= -1
         score_b += 1
         pen.clear()
         pen.write("player1: {}                          player2: {}".format(score_a,score_b),align="center",font=(20))
         
    if q.ycor() < -300 :
       q.sety(-300)
       q.dy *= -1

    elif q.ycor() > 300 :
       q.sety(300)
       q.dy *= -1
           
    y1 = a.ycor()
    
    if q.xcor() == a.xcor()  and q.ycor()<= y1 + 100 and q.ycor()>= y1 -100:        #paddle ball collision
        q.dx *= -1
        q.dy *= 1
  
    
    j = f.ycor()
    
   
    if q.xcor() == f.xcor() and q.ycor() <= j + 100 and q.ycor() >= j - 100  :
       
        q.dx *= -1
        q.dy *= 1

    if score_a==n or score_b==n:
        pen.goto(0,-200)
        if score_a==n:
            pen.write((name1, "wins"),align="center",font=("Ariel Black",24,"bold","italic"))
        elif score_b==n:
            pen.write((name2,"wins"),align="center",font=("Ariel Black",24,"bold","italic"))
        run=False


values=(name1,name2,score_a,score_b,joining_time,date)
mydb=mysql.connector.connect(host='localhost',database='pong',user='root',passwd='nikhil')      #data entry in sql
mycursor=mydb.cursor()
mycursor.execute("insert into entries values('%s','%s',%s,%s,'%s','%s')"%values)
mydb.commit()
