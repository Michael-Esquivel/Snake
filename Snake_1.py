import pygame, time, random

pygame.init() #Inicializa componentes de Pygame y evita posibles errores

play_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")     #Title
fps = pygame.time.Clock()

def food_spawn():
    food_pos = [random.randint(0,49)*10, random.randint(0,49)*10]   #El 10 la ubica cada 10 pixeles, este numero se igualo al tamaño del
    return food_pos

def main():
    snake_pos = [100,50]    #Cabeza es invisible
    snake_body = [[100,50], [100,50],[80,50]]
    direction = "RIGHT"
    change = direction
    food_pos = food_spawn()
    score = 0

    run = True
    while run:
        for event in pygame.event.get():    #".event.get()" detecta cualquier acción en el juego
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:    #"KEYDOWN:" Detecta cuando se pulsa cualquier boton
                    if event.key == pygame.K_RIGHT:
                        change = "RIGHT"
                    if event.key == pygame.K_LEFT:
                        change = "LEFT"
                    if event.key == pygame.K_UP:
                        change = "UP"
                    if event.key == pygame.K_DOWN:
                        change = "DOWN"

        if change == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"
        if change == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change == "UP" and direction != "DOWN":
            direction = "UP"
        if change == "DOWN" and direction != "UP":
            direction = "DOWN"


        if direction == "RIGHT":
            snake_pos[0] += 10
        if direction == "LEFT":
            snake_pos[0] -= 10
        if direction == "UP":
            snake_pos[1] -= 10
        if direction == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))   #Añade el ultimo cuerpo al primer indice, el que queda cerca a la cabeza
        if snake_pos == food_pos:       #Posicion cabeza es igual a posicion fruta, al no entrar al Else no se elimina la cola, por lo que se incrementaria el cuerpo del snake
            food_pos = food_spawn()
            score += 1
        else:
            snake_body.pop()    #Borra cola del snake, osea, borra lo que este en la ultima posicion

        play_surface.fill((0,0,0))  # Borra el rastro que va dejando

        for pos in snake_body:
            pygame.draw.rect(play_surface, (200,0,3), (pos[0], pos[1], 10, 10))  #Dibuja la serpiente    (surface, color, rect)     (x, y, w,h)
            #En el for con respecto a los POS, lo que hace es esto "snake_body[pos][0]"

        pygame.draw.rect(play_surface, (255,160,60), (food_pos[0], food_pos[1], 10, 10)) #Dibuja la fruta


        if snake_pos[0] >= 500 or snake_pos[0] <=0:
            print(f"Game Over! Score: {score})")
            run = False
        if snake_pos[1] >= 500 or snake_pos[1] <=0:
            print(f"Game Over! Score: {score})")
            run = False

        if snake_pos in snake_body[1:]: #Todos los corchetes del snake_body menos el primero
            print(f"Game Over! Score: {score})")
            run = False

        pygame.display.flip()   #Actualiza pantalla
        fps.tick(20)            

        

main()
pygame.quit()