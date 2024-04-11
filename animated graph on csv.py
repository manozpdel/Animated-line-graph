import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np

# Load data from CSV
df = pd.read_csv("modified_data.csv")
x = df['x'].values
num_columns = len(df.columns) - 1  # Exclude 'x' column

# Interpolate data for smoother animation
x_i = np.linspace(min(x), max(x), 500)
y_i = {}
for column in df.columns[1:]:
    y_i[column] = np.interp(x_i, x, df[column].values)

# Create figure and axes
fig, ax = plt.subplots()

# Plot initial lines
lines = [ax.plot([], [], label=column)[0] for column in df.columns[1:]]

# Initialize text annotations
texts = [ax.text(1, 1, '', color=line.get_color()) for line in lines]

def myupdating(i):
    if i < len(x_i):  # Check if i is within bounds
        # Update data for lines
        for line, column in zip(lines, df.columns[1:]):
            line.set_data(x_i[:i], y_i[column][:i])

        # Update position and text for annotations using loops
        for txt, column in zip(texts, df.columns[1:]):
            txt.set_position((x_i[i], y_i[column][i]))
            txt.set_text(str(i))
        
        if i == len(x_i) - 1:  # Check if animation is completed
            return False  # Stop the animation
    return True

# Create the animation
myanimation = FuncAnimation(fig, myupdating, frames=range(0, 501), interval=50)

# Set axis limits
ax.set_xlim(min(x), max(x))
ax.set_ylim(df.iloc[:, 1:].values.min(), df.iloc[:, 1:].values.max())

# Display legend
ax.legend()

# Display the animation
plt.show()
