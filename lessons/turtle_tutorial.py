"""This program creates a stain glass window scene using Turtle graphics."""
__author__: str = '730701948'

import turtle

def draw_square(turtle_prt1: turtle.Turtle, size: int) -> None:
    """Drawing a square."""
    for _ in range(4):
        turtle_prt1.forward(size)
        turtle_prt1.right(90)

def draw_scene() -> None:
    """Draws a colorful scene using Turtle graphics."""
    window = turtle.Screen()
    window.bgcolor("pink")

    # Create turtle objects
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()

    # Draw two stain glass blue squares
    for i in range(2):
        turtle1.color("blue")
        turtle1.begin_fill()
        draw_square(turtle1, 100)
        turtle1.end_fill()
        turtle1.penup()
        turtle1.goto(150 * (i + 1), 0)
        turtle1.pendown()

    # Draw a stain glass red circle filled with yellow color
    turtle2.color("red", "yellow")
    turtle2.begin_fill()
    turtle2.circle(50)
    turtle2.end_fill()

# Main function
def main() -> None:
    """Main function to initialize Turtle graphics and draw the scene."""
    draw_scene()

# Enterance point
if __name__ == "__main__":
    main()
