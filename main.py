import pygame
import os

WIDTH, HEIGTH = 900, 500 #Declaradas constantes de anchura y altura
WIN = pygame.display.set_mode((WIDTH, HEIGTH)) #Creada ventana con ancho y alto
pygame.display.set_caption("First Game!") #Crear nombre de la ventana

WHITE = (255, 255, 255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window():
    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP, (300, 100)) #Dibujar una superficie. Para poner texto o imágenes. 
    WIN.blit(RED_SPACESHIP, (700, 100))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()