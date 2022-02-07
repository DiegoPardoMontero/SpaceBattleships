import pygame
import os

WIDTH, HEIGTH = 900, 500 #Declaradas constantes de anchura y altura
WIN = pygame.display.set_mode((WIDTH, HEIGTH)) #Creada ventana con ancho y alto
pygame.display.set_caption("First Game!") #Crear nombre de la ventana

WHITE = (255, 255, 255)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):
    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #Dibujar una superficie. Para poner texto o imágenes. 
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]: #Move to the left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:
        yellow.x += VEL
    if keys_pressed[pygame.K_s]:
        yellow.y += VEL
    if keys_pressed[pygame.K_w]:
        yellow.y -= VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: #Move to the left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        red.x += VEL
    if keys_pressed[pygame.K_DOWN]:
        red.y += VEL
    if keys_pressed[pygame.K_UP]:
        red.y -= VEL

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()