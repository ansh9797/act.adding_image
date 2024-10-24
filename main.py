import pygame

pygame.init()

window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

image = pygame.image.load('C:\\Users\\alouk\\OneDrive\\Desktop\\Screenshots\\Screenshot 2024-10-17 205958.png')
image = pygame.transform.scale(image, (300, 300))

background_color = (58, 58, 58)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill(background_color)
    screen.blit(image, (100, 100))

    pygame.display.flip()

pygame.quit()