import pygame, random

class Cuerpo:
    def __init__(self, window):     #__init__ es un metodo constructor e inicializa atributos de ciertas variables. Toda clase en python le sigue un constructor
        self.x = 0
        self.y = 0
        self.window = window
        self.dir = 0  # 0 right, 1 left, 2 down, 3 up

    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (self.x, self.y, 10, 10))

    def movement(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10

class food:
    def __init__(self, window):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, 10, 10))

    def relocate(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        

def redraw(window):     #Redibuja Fondo, Comida y Serpiente en ese orden
    pygame.display.update()
    window.fill((0, 0, 0))
    comida.draw()
    
    for i in range(len(snake)):
        snake[i].draw()
        
    

def snake_ubicacion():  #Cuerpo sigue cabeza(snake[0])
    if(len(snake)) > 1:
        for i in range(len(snake)-1):
            snake[len(snake)-i-1].x = snake[len(snake)-i-2].x   #El Ultimo tendra la posicion del penultimo...
            snake[len(snake)-i-1].y = snake[len(snake)-i-2].y

def Colision():
    hit = False
    if (len(snake)) > 1:
        for i in range(len(snake)-1):    #Si no tuviese -1, agregaria un elemento demas en "snake[i + 1]" y marcaria error. exe: hay 5 elementos y +1 da 6, como no hay 6 elementos, arroja error
            if snake[0].x == snake[i + 1].x and snake[0].y == snake[i + 1].y:       #Si Cabeza toca alguna parte del cuerpo, reinicia el juego
                hit = True

    
    return hit

def main():
    global comida, snake
    window = pygame.display.set_mode((400, 400))
    window.fill((0, 0, 0))
    pygame.display.set_caption("Snake")
    snake = [Cuerpo(window)]
    snake[0].draw()
    comida = food(window)
    run = True
    velocidad = 100
    while run:
        for event in pygame.event.get():    #".event.get()" detecta cualquier acción en el juego
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:    #"KEYDOWN:" Detecta cuando se pulsa cualquier boton
                if event.key == pygame.K_DOWN:
                    snake[0].dir = 2
                if event.key == pygame.K_LEFT:
                    snake[0].dir = 1
                if event.key == pygame.K_RIGHT:
                    snake[0].dir = 0
                if event.key == pygame.K_UP:
                    snake[0].dir = 3
        snake_ubicacion()
        snake[0].movement()
        redraw(window)
        pygame.time.delay(velocidad)
    
        if snake[0].x >= 400:   #Si toca borde, aparece al otro lado
            snake[0].x = 0
        elif snake[0].x < 0:
            snake[0].x = 390

        if snake[0].y >= 400:
            snake[0].y = 0
        elif snake[0].y < 0:
            snake[0].y = 390

        if Colision():
            snake = [Cuerpo(window)]
            comida.relocate()
            velocidad = 100

        if snake[0].x == comida.x and snake[0].y == comida.y:
            if velocidad > 35:
                velocidad -= 5
            comida.relocate()
            snake.append(Cuerpo(window))


main()
pygame.quit()

