import turtle, random
screen = turtle.Screen()
screen.bgcolor('black')

snowflakes = []

for _ in range(50):
    snowflake = turtle.Turtle()
    snowflake.shape('turtle')
    snowflake.color('white')
    snowflake.penup()
    snowflake.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(200, 400)
    snowflake.goto(x,y)
    snowflake.dy = random.randint(10, 30)
    snowflakes.append(snowflake)

while True:
    for snowflake in snowflakes:
        snowflake.sety(snowflake.ycor()-snowflake.dy)

        if snowflake.ycor()<-300:
            snowflake.sety(400)

snowflake.hideturtle()
turtle.done()