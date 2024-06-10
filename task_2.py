"""Module providing a function drawing Pythagoras Tree Fractal."""
import turtle

def draw_tree(t, branch_length, level, angle):
    """Function drawing Pythagoras Tree Fractal."""
    if level == 0:
        return

    t.forward(branch_length)

    # Save the current turtle position and heading
    current_pos = t.position()
    current_heading = t.heading()

    # Draw the right branch
    t.right(angle)
    draw_tree(t, branch_length * 0.7, level - 1, angle)

    # Restore the turtle position and heading for the left branch
    t.setposition(current_pos)
    t.setheading(current_heading)

    # Draw the left branch
    t.left(angle)
    draw_tree(t, branch_length * 0.7, level - 1, angle)

    # Restore the initial position and heading
    t.setposition(current_pos)
    t.setheading(current_heading)

def main():
    """Main module function"""
    # Initialize screen and turtle
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    t = turtle.Turtle()
    t.speed(0)  # Maximum speed

    # Initial parameters
    initial_branch_length = 100
    recursion_level = int(input("Enter recursion level: "))
    initial_angle = 30

    # Initial turtle position
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    # Draw the Pythagoras Tree
    draw_tree(t, initial_branch_length, recursion_level, initial_angle)

    # Finish drawing
    screen.mainloop()

if __name__ == "__main__":
    main()
