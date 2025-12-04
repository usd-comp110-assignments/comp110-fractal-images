"""
Fractal Tree (Turtle) 
COMP 110 
"""
import turtle
import math

CANVAS_SIZE = 700
INITIAL_BRANCH_LENGTH = 300  # Initial branch length
TOTAL_RECURSION_DEPTH = 0    # Total levels of recursion
ANGLE_DELTA = 0              # Change in angle between branches (degrees)
LENGTH_SCALE = 0.0          # Scale factor for child branch lengths (0 < LENGTH_SCALE < 1)

def draw_fractal_tree(t, branch_length, remaining_levels_of_recursion):
    """
    Draw recursive fractal tree using turtle movements.

    Parameters:
    - t (type: turtle.Turtle): The turtle object used for drawing.  The turtle's position and heading are set up to 
                    start drawing the current branch. 
    - branch_length (type: float): The length of the current branch.
    - remaining_levels_recursion (type: int): Remaining levels of recursion, including 
                    the current branch.

    Returns: None.
       On returning, the turtle's position and heading are restored to the same as when the function was called.
    """
   

    # conditional for recursive case
    pass # Replace this

    # draw the current branch
    pass  # Replace this 

    # draw the left subtree:
    # make sure turtle position and heading and set up for drawing the left subtree.
    pass  # Replace this 
    # recursive call to draw the left subtree
    pass  # Replace this 

    # draw the right subtree:
    # make sure turtle position and heading and set up for drawing the right subtree.
    pass  # Replace this 
    # recursive call to draw the right subtree
    pass  # Replace this 

    # restore heading and position to what it was at the start of the function.
    pass  # Replace this 

    # Base case
    pass # Replace with what is needed

def initialize_turtle():
    """
    Initializes the turtle graphics window and turtle.
    
    Returns:
    (type: tuple), (screen, t): 
    - screen: The turtle Screen object.
    - t: The turtle Turtle object.
    
    """

    # Initialize the turtle graphics window and turtle.
    screen = turtle.Screen()
    screen.setup(CANVAS_SIZE, CANVAS_SIZE)
    screen.title("Fractal Tree (Turtle) - Solution")

    # Speed up drawing: disable animation and update once at the end
    #screen.tracer(0, 0)

    # Create the turtle
    t = turtle.Turtle()
    #t.hideturtle()
    t.speed(0)

    # Start pointing up from near the bottom
    t.left(90)
    t.penup()
    t.goto(0, -CANVAS_SIZE // 2 + 30)
    t.pendown()

    return screen, t


def main():
    # Initialize turtle graphics
    screen, t = initialize_turtle()

    # Draw the fractal tree
    draw_fractal_tree(t, INITIAL_BRANCH_LENGTH, TOTAL_RECURSION_DEPTH)

    # finish drawing and show it
    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()
