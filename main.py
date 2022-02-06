import pygame

WIDTH, HEIGTH = 900, 500 #Declaradas constantes de anchura y altura
WIN = pygame.display.set_mode((WIDTH, HEIGTH)) #Creada ventana con ancho y alto

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()