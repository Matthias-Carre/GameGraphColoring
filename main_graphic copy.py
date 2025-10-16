import turtle
from Grid import Grid

color_selection_x = 34
color_selection_y = 25

def color_selection():
    return None

def draw_rectangle(x, y, width, height, color):#draw rectangle form x,y to x+width,y+height
    turtle.penup()
    turtle.speed(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.penup()

def write_text(x, y, text, font_size=12):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, align="left", font=("Arial", font_size, "normal"))
    turtle.penup()


def color_choice():
    #legend to the right of the turtle window

    draw_rectangle(color_selection_x, color_selection_y, 5, 30, "black")

    colors = ["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN"]
    for i, color in enumerate(colors):
        write_text(color_selection_x + 0.5, color_selection_y + 30 - (i+1) * 4, color, font_size=12)

def setup_turtle_grid(grid):
    turtle.title("Graph Coloring Game")
    turtle.setup(width=800, height=600)
    turtle.setworldcoordinates(0, 0, 40, 60)
    turtle.speed(0)
    turtle.hideturtle()
    draw_rectangle(0, 0, 30, 60, "black")
    turtle.penup()
    color_choice()

def get_mouse_click(x, y):
    print(f"Mouse clicked at: ({x}, {y})")
    draw_rectangle(x, y, 1, 1, "red")
    #if(x > color_selection_x)
    
    

if __name__=="__main__":
    grid = Grid(5, 5)
    
    setup_turtle_grid(grid)
    turtle.onscreenclick(get_mouse_click)
    turtle.done()