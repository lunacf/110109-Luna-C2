import pygame
 
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont("Arial", 30)
text = font.render("Hello World", True, "RED")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse down at", event.pos)
        if event.type == pygame.KEYDOWN:
            print("Presionando")
            event.key = 97
            print("a")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    #A circe in the middle of the screen
                                     #x z y radius
    pygame.draw.circle(screen, "red", (screen.get_width()/2 - 50, screen.get_height()/2 -50), 100, 100)

    
    # If you want to change the text, you need to re-render it
    text = font.render("Hello World", True, "RED")
    #Write text on the screen
    screen.blit(text, (600, 300))


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()