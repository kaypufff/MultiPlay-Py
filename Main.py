import pygame

# initializes pygame
pygame.init()

main_screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("MultiPlay-Py")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    # Main Screen Background Color
    main_screen.fill((0, 0, 0))
    pygame.display.update()