import os
import time
import random
import msvcrt  # For Windows. Use 'import sys, tty, termios' for Unix-based systems

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_key_pressed():
    return msvcrt.kbhit()

def get_key():
    return msvcrt.getch().decode('utf-8')

def draw_game(bird_y, pipes, score):
    screen = [[' ' for _ in range(20)] for _ in range(20)]
    
    # Draw bird
    screen[bird_y][5] = '>'
    
    # Draw pipes
    for pipe in pipes:
        for y in range(20):
            if y < pipe[1] or y > pipe[1] + 3:
                screen[y][pipe[0]] = '|'
    
    # Draw screen
    print('\n'.join(''.join(row) for row in screen))
    print(f"Score: {score}")

def main():
    bird_y = 10
    velocity = 0
    pipes = []
    score = 0
    frame = 0

    while True:
        clear_screen()
        
        # Bird physics
        bird_y += velocity
        velocity += 0.5
        
        # Check for jump
        if is_key_pressed():
            key = get_key()
            if key == ' ':
                velocity = -1
        
        # Generate pipes
        if frame % 20 == 0:
            pipes.append([19, random.randint(0, 16)])
        
        # Move pipes
        for pipe in pipes:
            pipe[0] -= 1
        
        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe[0] >= 0]
        
        # Check for collisions
        for pipe in pipes:
            if pipe[0] == 5 and (bird_y < pipe[1] or bird_y > pipe[1] + 3):
                print("Game Over!")
                return
            elif pipe[0] == 5:
                score += 1
        
        # Check for out of bounds
        if bird_y < 0 or bird_y >= 20:
            print("Game Over!")
            print(score)
            return
        
        draw_game(int(bird_y), pipes, score)
        
        frame += 1
        time.sleep(0.1)

if __name__ == "__main__":
    main()