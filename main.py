import arcade

# Read data from the file
data = []

with open("data") as file:
    for line in file:
        state, population, change = line.strip("\n").split(',')
        data.append((state, int(population), int(change)))


# Initialize the window
window = arcade.Window(800, 600, "Project 4", False, True)
arcade.set_background_color(arcade.color.BEIGE)
arcade.start_render()

# Define the starting x-coordinate
x = 50

# Draw the bars and text
for state, population, change in data:
    bar_height = population / 70000  # Scale population to the number of pixels

    # Calculate the color based on percentage change
    percentage_change = change / population * 100
    if percentage_change < -0.5:
        color = arcade.color.RED
    elif percentage_change < 0:
        color = arcade.color.ORANGE
    elif percentage_change < 0.5:
        color = arcade.color.YELLOW
    elif percentage_change < 1:
        color = arcade.color.YELLOW_GREEN
    else:
        color = arcade.color.GREEN

    # Draw the bar
    arcade.draw_rectangle_filled(x, 0, 70, bar_height, color)

    # Draw the state name
    state_label = arcade.Text(state,x-50,bar_height, arcade.color.BLACK)

    state_label.draw()


    # Adjust x-coordinate for the next state
    x += 100

arcade.finish_render()

# Run the application
arcade.run()