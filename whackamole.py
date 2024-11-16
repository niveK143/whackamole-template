import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        black = (10,10,10)
        running = True
        x,y = 0,0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    clicked_col = mouse_x // 32
                    clicked_row = mouse_y // 32

                    if (clicked_col * 32, clicked_row * 32) == (x, y):
                        x = random.randrange(0, 20) * 32
                        y = random.randrange(0, 16) * 32
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            for i in range (0,20):
                x1 = i * 32
                pygame.draw.line(screen, black, (x1,0), (x1,512))
            for i in range (0,16):
                y1 = i * 32
                pygame.draw.line(screen, black, (0,y1), (640,y1))



            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
