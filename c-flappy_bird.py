import curses
from random import randint

def main(screen):
    # Initialize the screen
    curses.curs_set(0)
    sh, sw = screen.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Initial settings
    snk_x = sw // 4
    snk_y = sh // 2
    bird = [[snk_y, snk_x]]
    score = 0

    # Create obstacles
    obstacles = []
    for i in range(5):
        obstacle_x = sw + i * 10
        obstacle_hole = randint(3, sh - 4)
        obstacles.append([obstacle_x, obstacle_hole])

    # Game logic
    ESC = 27
    key = curses.KEY_RIGHT
    key = curses.KEY_UP
    while key != ESC:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Bird movement
        if key == curses.KEY_UP:
            snk_y = max(1, snk_y - 1)
        else:
            snk_y = min(sh - 2, snk_y + 1)

        bird = [[snk_y, snk_x]]

        # Move obstacles
        new_obstacles = []
        for obstacle in obstacles:
            obstacle[0] -= 1
            if obstacle[0] > 0:
                new_obstacles.append(obstacle)
            else:
                score += 1
                obstacle_x = sw - 1
                obstacle_hole = randint(3, sh - 4)
                new_obstacles.append([obstacle_x, obstacle_hole])
        obstacles = new_obstacles

        # Collisions
        if bird[0][0] in [0, sh] or bird[0][1] in [0, sw]:
            break

        for obstacle in obstacles:
            if bird[0][1] == obstacle[0] and (bird[0][0] < obstacle[1] or bird[0][0] > obstacle[1] + 3):
                key = ESC
                break

        # Refresh screen
        w.clear()
        w.border(0)
        w.addstr(0, 2, f'Score: {score}')
        w.addch(bird[0][0], bird[0][1], curses.ACS_PI)

        for obstacle in obstacles:
            for y in range(sh):
                if y < obstacle[1] or y > obstacle[1] + 3:
                    if y > 0 and y < sh - 1 and obstacle[0] < sw - 1:
                        w.addch(y, obstacle[0], curses.ACS_CKBOARD)

        w.refresh()

    # End game
    curses.endwin()
    print(f'Final Score: {score}')

# Run the game
curses.wrapper(main)
