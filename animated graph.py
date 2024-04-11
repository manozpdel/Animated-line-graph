import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial data
x = [1, 2, 3,4,5,6]
y = [1, 2, 5,3,6,9]
y2 = [1, 5, 3,4,9,10]

# Interpolate data for smoother animation
x_i = np.linspace(1, 6, 500)
y_i = np.interp(x_i, x, y)
y2_i = np.interp(x_i, x, y2)

# Create figure and axes
fig, ax = plt.subplots()

# Plot initial lines
line, = ax.plot(x, y, color='r')
line2, = ax.plot(x, y2, color='b')

# Initialize text annotations
text = ax.text(1, 1, '', color='r')
text2 = ax.text(1, 1, '', color='b')


# Define the function to update the plot for each frame
def myupdating(i):
    if i < len(x_i):  # Check if i is within bounds
        # Update data for lines
        line.set_data(x_i[:i], y_i[:i])
        line2.set_data(x_i[:i], y2_i[:i])

        # Update position and text for annotations
        text.set_position((x_i[i], y_i[i]))
        text.set_text(str(i))
        text2.set_position((x_i[i], y2_i[i]))
        text2.set_text(str(i))



# Create the animation
myanimation = FuncAnimation(fig, myupdating, frames=501, interval=20)

# Display the animation
plt.show()
