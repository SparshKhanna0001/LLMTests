import cmd
from cmd import *

# Initialize the command prompt
prompt = Prompt()

# Set the title of the window
title = "Flappy Bird"

# Set the game variables
gravity = 0.5
bird_speed = 10
is_jumping = False
score = 0

# Create a list of pipes
pipes = []

# Main game loop
while True:
    # Handle events
    for event in prompt.get_events():
        if event == " ":
            is_jumping = True
        elif event == "ESC":
            break

    # Update game state
    if is_jumping:
        bird_y -= gravity
    else:
        bird_y += gravity

    # Check for collision with pipes
    for pipe in pipes:
        if pipe.get_position() <= bird_y + bird_image.get_height() and pipe.get_position() >= bird_y:
            is_jumping = False
            bird_speed = 0
            score += 1
            pipes.remove(pipe)

    # Update the screen
    prompt.clear_screen()
    prompt.set_title(title)
    for pipe in pipes:
        prompt.print_line(f"{pipe.get_position()} {pipe.get_size()}")
        prompt.print_line(f"Bird position: {bird_y} Bird speed: {bird_speed} Score: {score}")
        if is_jumping:
            prompt.print_line("Jump!")
        else:
            prompt.print_line("Flap!")

# Clean up
prompt.clean_up()