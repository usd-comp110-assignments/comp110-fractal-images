"""
Generic Fractal Drawer - Instructor Solution
COMP 110 - Recursion and Fractals

This file contains a complete solution for the turtle-based fractal tree.
It includes small visual improvements and a performance tip (turn off tracer).
"""
import turtle
import math

CANVAS_SIZE = 800

import turtle

def draw_fractal(t, length, angle, level, instructions, 
                 target1, sub_instructions1, target2, sub_instructions2, scale_factor):
    """
    Draws a fractal defined by the function parameters.

    Parameters:
    - t (type: turtle.Turtle): The turtle object used for drawing.
    - length (type: int): The distance the turtle will travel when given a forward or backward command.
    - angle (type: int): The angle to turn when the turtle is told to turn left or right.
    - level (type: int) Remaining levels of recursion.  When the level becomes negative (-1), do nothing and just return.
    - instructions (type: str): The string encoding the instructions that the function should follow.  Each character of 
      the string is an instruction, and the instructions are executed in order (left to right).   The meaning of each 
      instruction is given further below.
    - target1 (type: str): target1 is an instruction (so it is a single character). 
      If  level > 0, then draw_fractal executes target1 by making a recursive call with all parameters the same, except:
          The instructions parameter is replaced by the sub_instructions1 parameter.
          length is scaled by the scale_factor parameter.
          level is decreased by 1.  
      If level == 0 and target1 is a turtle instruction (see below), then the turtle instruction is executed, and otherwise it is ignored.
    - sub_instructions1 (type: str): The string describing the instructions to pass in the recursive call, when  target1 is 
      encountered in instructions with level > 0.
    - target2 (type: str): target2 is an instruction (so it is a single character). 
      If  level > 0, then draw_fractal executes target2 by making a recursive call with all parameters the same, except:
          The instructions parameter is replaced by the sub_instructions2 parameter.
          length is scaled by the scale_factor parameter.
          level is decreased by 1.  
      If level == 0 and target2 is a turtle instruction (see below), then the turtle instruction is executed, and otherwise target2 is ignored.
    - sub_instructions2 (type: str): The string describing the instructions to pass in the recursive call, when  target2 is encountered in 
      instructions with level >0.
    - scale_factor (type: float): The amount to scale the length parameter by when a recursive call is made.
    
    The turtle instructions are:        
        'F' : move the turtle forward by length
        'B' : move the turtle backward by length
        'R' : turn the turtle right by angle
        'L' : turn the turtle left by angle

    Returns: None.
    """
    pass # Replace with your function implementation.

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
    t.goto(0, 0)
    t.pendown()

    return screen, t

def main():
    # Instructions for different fractals.
    # Each tuple contains the parameters to be passed into
    # draw_fractal, in the same order as required by the function, starting
    # with length.  So 
    # format = (length, angle, level, instructions, target1, sub_instructions1, 
    #           target2, sub_instructions2, scale_factor)

    fractal_instructions = [
        # 1. Fractal tree
        # Needs to shrink (0.7) to look organic. Started length at 80 so it's visible.
        (80, 20, 6, "X", "X", "FLXRRXLB", "#", "", 0.7),

        # 2. Koch Snowflake
        # Needs to shrink by exactly 1/3 (0.3333) to maintain the shape.
        # Start length large (300) because it shrinks rapidly.
        (300, 60, 3, "FRRFRRF", "F", "FLFRRFLF", "#", "", 1/3),

        # 3. Levy C Curve
        # Scale 1.0 (It grows), so start with small length (5).
        (5, 45, 10, "F", "F", "LFRRFL", "#", "", 1.0),

        # 4. Dragon Curve
        # Scale 1.0 (It grows), so start with small length (5).
        (5, 90, 10, "FX", "X", "XRYF", "Y", "FXLY", 1.0),

        # 5. Hilbert Curve
        # Scale 1.0 (It grows), so start with small length (10).
        (10, 90, 5, "X", "X", "LYFRXFXRFYL", "Y", "RXFLYFYLFXR", 1.0)
    ]

    # Get user selection
    while True:
        try:
            choice = int(input("""Choose fractal to draw:\n simple tree: 0\n snowflake: 1
 levy-c: 2\n dragon curve: 3\n Hilbert curve: 4\nYour choice: """))
            if 0 <= choice <= 4:
                break
            else:
                print("Invalid selection.  Try again.")
        except:
            print("Invalid selection.  Try again.")

    # Initialize turtle graphics
    screen, t = initialize_turtle()

    # Draw the fractal tree, passing the instructions for the user chosen fractal.
    # The syntax *fractal_instructions[choice] expands the tuple containing the
    # parameters so they are passed as additional parameters to the function.
    draw_fractal(t, *fractal_instructions[choice])

    # finish drawing and show it
    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()
