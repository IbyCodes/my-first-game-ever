
import turtle  # turtle is a pre-installed Python library that enables users to create pictures and shapes by providing them with a virtual canvas)
import winsound

window = turtle.Screen()  # needed to pop up a screen when the code is ran
window.title("Pong Game by IbytheGOAT")  # window name
window.bgcolor("black")   # this will be the background color of the game
window.setup(width=800, height=600)  # this will be the size of the window
window.tracer = (0)   # stops the window from updating


# paddle 1


paddle_a = turtle.Turtle()
# needs to be 0 or else the game will be very slow (animation speed)
paddle_a.speed(0)
paddle_a.shape("square")   # this will be the shape of the paddle
paddle_a.color("white")    # color of the paddle
# This will stretch out the paddle by 5x in width, and same size in length( by default it was 20 pixels x 20 pixels)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# this will prevent lines being drawn every time there is some movement on the screen
paddle_a.penup()
# this will put the paddle at the very left side of the screen
paddle_a.goto(-350, 0)


# paddle 2

paddle_b = turtle.Turtle()
paddle_b.speed(0)   # needs to be 0 or else the game will be very slow
paddle_b.shape("square")   # this will be the shape of the paddle
paddle_b.color("white")    # color of the paddle
# This will stretch out the paddle by 5x in width, and same size in length( by default it was 20 pixels x 20 pixels)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# this will prevent lines being drawn every time there is some movement on the screen
paddle_b.penup()
# this will put the paddle at the very left side of the screen
paddle_b.goto(350, 0)


# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # middle of the screen
# means that everytime the ball moves, it will move by 4 pixels in x direction  ( this must be altered depending on the computer)
ball.dx = 4
ball.dy = -4   # means that everytime the ball moves, it will move by 4 pixels in y direction


# Functions for movement of the paddles
def paddle_a_up():
    y = paddle_a.ycor()   # .ycor is from the turtle module. It returns the y coordinate
    y += 20  # this will add 20 to the y coordinate
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()   # .ycor is from the turtle module. It returns the y coordinate
    y -= 20  # this will subtract 20 to the y coordinate
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()   # .ycor is from the turtle module. It returns the y coordinate
    y += 20  # this will add 20 to the y coordinate
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()   # .ycor is from the turtle module. It returns the y coordinate
    y -= 20  # this will subtract 20 to the y coordinate
    paddle_b.sety(y)


# Binding the keyboard controls to the game

window.listen()  # the window will "listen" to the keyboard

# the function paddle_a_up will be called when w is pressed, causing the y coordinate of the paddle to increase by 20
window.onkeypress(paddle_a_up, "w")

# when s is pressed, player #1 paddle will decrease in y coordinate by 20
window.onkeypress(paddle_a_down, "s")


window.onkeypress(paddle_b_up, "Up")  # up arrow on keyboard (player 2)
window.onkeypress(paddle_b_down, "Down")  # down arrow on keyboard (player 2)


# Note THAT testing is VERY important. TEST every TIME a new element/object is added to the game

# Adding the scoring system to the screen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()  # we don't want to actually see the pen, just want to see its text
pen.goto(0, 260)  # these are the coordinates of the score on the screen
pen.write("Player A: 0 Player B: O", align="center",
          font=("Courier", 24, "bold"))


# making the scoring system actually add up and work:
score_a = 0
score_b = 0  # initial scores


# moving the ball


# every game needs this ( BUT PLEASE LOOP IT AT THE VERY END)
while True:
    window.update()  # now every time the loop runs, it will update the screen

    ball.setx(ball.xcor() + ball.dx)  # this is to move the ball (x direction)

    # this is also to move the ball (y direction)
    ball.sety(ball.ycor() + ball.dy)


# Creating the bounce off the border

    if ball.ycor() > 290:  # this will reverse the direction of the ball when it hits higher then +290 (y direction) (top border)
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(
            "C:\\Users\\ibrah\\OneDrive\\Desktop\\Coding Practice\\Python\\Python Games\\bamboo.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:  # this will reverse the direction of the ball when it hits lower then -290 (y direction) (bottom border)
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(
            "C:\\Users\\ibrah\\OneDrive\\Desktop\\Coding Practice\\Python\\Python Games\\bamboo.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:     # remember that the width is 800, so 400 , 400 (this is for right border)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1   # this will add 1 to player 1's score, as it's gone off the screen due to player 2 missing it
        pen.clear()   # this will help with the score to not write over itself, and instead have one number for each player's score
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound(
            "C:\\Users\\ibrah\\OneDrive\\Desktop\\Coding Practice\\Python\\Python Games\\nope.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:     # remember that the width is 800, so 400 , 400  ( this is for left border)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1  # this will add 1 to player 2's score, as it's gone off the screen due to player 1 missing it
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound(
            "C:\\Users\\ibrah\\OneDrive\\Desktop\\Coding Practice\\Python\\Python Games\\nope.wav", winsound.SND_ASYNC)


# making the ball bounce off the paddles

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(
            "C:\\Users\\ibrah\\OneDrive\\Desktop\\Coding Practice\\Python\\Python Games\\bamboo.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(
            "C:\\Users\\ibrah\\OneDrive\\Desktop\\Coding Practice\\Python\\Python Games\\bamboo.wav", winsound.SND_ASYNC)
