"""
Koch snowflake 
COMP 110 - Recursion and Fractals
"""

import turtle

CANVAS_SIZE = 800
INITIAL_SEGMENT_LENGTH = 400  # Initial length of a Koch segment
TOTAL_RECURSION_DEPTH = 6  # Total levels of recursion

def draw_koch_segment(t, length, remaining_levels_of_recursion):
    """
    Recursively draw on segment of the Koch snowflake.

    Parameters:
    - t (type: turtle.Turtle): The turtle object used for drawing.  The turtle's position and heading are set up to 
                    to begin drawing the segment. 
    - length (type: float): The length of the segment (if it were draw as a single line).
    - remaining_levels_recursion (type: int): Remaining levels of recursion, including 
                    the current level.

    Returns: None.   On returning, the direction of the turtle should be the same as when the function was called,
           and the position of the turtle should be length from its starting position, having moved in the direction
           it had at the start of the function.
    """
    
    pass # Replace this with your implementation of the function.

def draw_koch_snowflake(t, segment_length, levels_of_recursion):
    """
    Draw a Koch snowflake by drawing three Koch segments, one for each side
    of an equilateral triangle.

    Parameters:
    - t (type: turtle.Turtle): The turtle object used for drawing.  The turtle's position and heading are set up to 
                    to begin drawing the first segment. 
    - segment_length (type: float): The length of each segment (if it were draw as a single line).
    - levels_of_recursion (type: int): Total levels of recursion for each segment.

    Returns: None.
    """
     
    for _ in range(3):
        draw_koch_segment(t, segment_length, levels_of_recursion)
        t.right(120) 

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

    # Start pointing up
    t.left(90)
    t.penup()
    t.goto(-CANVAS_SIZE // 8, -CANVAS_SIZE // 4)
    t.pendown()

    return screen, t

def main():
    # Initialize turtle graphics
    screen, t = initialize_turtle()

    # Draw the koch snowflake.
    draw_koch_snowflake(t, INITIAL_SEGMENT_LENGTH, TOTAL_RECURSION_DEPTH)

    # finish drawing and show it
    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()
