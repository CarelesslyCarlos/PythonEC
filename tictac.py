import pygame
from pygame.locals import *

pygame.init()

# create blank game window
grid_width = 2
marks_width = 7
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

# Define colors
x_color = (204, 0, 0)
o_color = (0, 128, 255)
replay_text_color = (101, 53, 15)
replay_rect_color = (128, 71, 28)

# Define Fonts
font = pygame.font.SysFont('casc', 34)

# Define a rectangle for the "play again" option
replay_rect = Rect(screen_width // 2 -80, screen_height // 2, 160, 50)

# Variables
markers = []
clicked = False
pos = []
player = 1
winner =  0
game_over = 0


# Create a "3x3" list of lists to represent the game board cells
for x in range(3):    
    row = [0] * 3
    markers.append(row)

def draw_grid():
    bg = (154, 123, 79) 
    grid = (101, 53, 15) 
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), grid_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), grid_width)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, x_color, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), marks_width)
				pygame.draw.line(screen, x_color, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), marks_width)
			if y == -1:
				pygame.draw.circle(screen, o_color, (x_pos * 100 + 50, y_pos * 100 + 50), 38, marks_width)
			y_pos += 1
		x_pos += 1

def check_winner():
    
    global winner
    global game_over
    y_pos = 0
    for x in markers:
        # Check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        # Check rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    # Check diagonal rows for determining who da winner
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True
        
    # Check for a tie
    if game_over == False:
        tie = True
        for row in markers:
            for i in row:
                if i == 0:
                    tie = False
        # if there is a tie, then call game over and set winner to 0
        if tie == True:
            game_over = True
            winner = 0

def draw_winner(winner):
    if winner != 0:
        win_text = f"Player {winner} wins!"
    elif winner == 0:
        win_text = "u both suck! TIE"
        
    win_img = font.render(win_text, True, x_color)
    pygame.draw.rect(screen, o_color, (screen_width // 2 - 100, screen_height // 2 - 50, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    replay_text = "Play again?"
    replay_img = font.render(replay_text, True, x_color)
    pygame.draw.rect(screen, o_color, replay_rect)
    screen.blit(replay_img, (screen_width // 2 - 80, screen_height // 2 + 10))

# Main loop
run = True
while run:

    # Draw board and markers
    draw_grid()
    draw_markers()

    # add event handlers
    for event in pygame.event.get():
        # Handle exit
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
        # Check for mouseclick
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if markers[cell_x][cell_y] == 0:
                    markers[cell_x][cell_y] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner(winner)
        # Check for mouse click to see if clicked on PLay again

        # Check for mouseclick
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if replay_rect.collidepoint(pos):
                # Reset all variables
                markers = []
                pos = []
                player = 1
                winner =  0
                game_over = 0
                for x in range(3):    
                    row = [0] * 3
                    markers.append(row)

    pygame.display.update()

pygame.quit()

