import turtle as t
import random
import colorgram

timmy_the_turtle = t.Turtle(shape="turtle")
t.colormode(255)



def draw_triangle():  
    for _ in range(3):
        timmy_the_turtle.right(120)
        timmy_the_turtle.forward(100)
        
        
        
def draw_square():
    for _ in range(4):
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)
        

def draw_dashed_line():
    for _ in range(15):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()
   
   
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)
        
        
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]       
def draw_cool_shape():
    for _ in range(3, 11):
        timmy_the_turtle.color(random.choice(colors))
        draw_shape(_)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0 ,255)
    return (r, g, b)


def random_walk():
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.speed("fastest")
    for _ in range(200):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.setheading(random.choice([0, 90, 180, 270]))
        timmy_the_turtle.forward(30)  
        

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
        

rgb_colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]        
def draw_hirst_painting():
    timmy_the_turtle.penup()
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.setheading(225)
    timmy_the_turtle.forward(300)
    timmy_the_turtle.setheading(0)
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        timmy_the_turtle.dot(20, random.choice(rgb_colors))
        timmy_the_turtle.forward(50)
        if dot_count % 10 == 0:
            timmy_the_turtle.setheading(90)
            timmy_the_turtle.forward(50)
            timmy_the_turtle.setheading(180)
            timmy_the_turtle.forward(500)
            timmy_the_turtle.setheading(0)
    
    
# print(rgb_colors)
# draw_cool_shape()
# random_walk()
# draw_dashed_line()
# draw_hirst_painting()


screen = t.Screen()
screen.exitonclick()


    

   



