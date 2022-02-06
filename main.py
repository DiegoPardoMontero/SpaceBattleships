import pygame

WIDTH, HEIGTH = 900, 500 #Declaradas constantes de anchura y altura
WIN = pygame.display.set_mode((WIDTH, HEIGTH)) #Creada ventana con ancho y alto
pygame.display.set_caption("First Game!") #Crear nombre de la ventana

WHITE = (255, 255, 255)

FPS = 60

def draw_window():
    WIN.fill((WHITE))
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