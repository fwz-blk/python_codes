import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)

# Function to draw a circle with a dot inside
def circle_with_dot(x, y, radius):
    # Draw circle
    pen.penup()
    pen.goto(x, y - radius)  # Move to starting point
    pen.pendown()
    pen.circle(radius)
    
    # Draw dot inside
    pen.penup()
    pen.goto(x, y - radius // 2)  # roughly center
    pen.dot(radius // 2, "black")

# Draw two side-by-side
circle_with_dot(-80, 0, 60)  # left
circle_with_dot(80, 0, 60)   # right

# Keep window open
screen.mainloop()
