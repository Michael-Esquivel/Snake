import pygame as pg, random

pg.init()
size = 30
size4 = size/4

w = 20 * size
h = 20 * size

screen = pg.display.set_mode((w, h))

def movements(movement, snakes):
    if movement == 'down':
        snakes[0][0].y += size
        snakes[0][1].y += size
    if movement == 'up':
        snakes[0][0].y -= size
        snakes[0][1].y -= size
    if movement == 'left':
        snakes[0][0].x -= size
        snakes[0][1].x -= size
    if movement == 'right':
        snakes[0][0].x += size
        snakes[0][1].x += size

def follow(snakes):
    size_config = size4/2

    for i in range(len(snakes)):
        if i > 0:
            snakes[-i][0].x = snakes[-i-1][0].x
            snakes[-i][0].y = snakes[-i-1][0].y

            if i < len(snakes)-1:   
                snakes[-i][1].x = snakes[-i-1][1].x
                snakes[-i][1].y = snakes[-i-1][1].y
            else:                                       #2do no hereda de la cabeza
                snakes[-i][1].x = snakes[-i-1][1].x + size_config
                snakes[-i][1].y = snakes[-i-1][1].y + size_config

def draw(sc, snakes, apple):
    screen.fill('black')
    
    pg.draw.rect(sc, 'red', apple)
    for snake in snakes:
        pg.draw.rect(sc, 'green', snake[0])
        pg.draw.rect(sc, 'blue', snake[1])

def collide(snakes):
    for i in range(len(snakes)-1):
        if snakes[0][0].x == snakes[i+1][0].x and snakes[0][0].y == snakes[i+1][0].y:
            return True


def main():
    clock = pg.time.Clock()
    x = 0
    y = 0
    size_config = size/8
    snake = [[pg.Rect(x, y, size, size), pg.Rect(x+size4, y+size4, size/2, size/2)]]
    movement = 'right'

    x_apple = random.randint(1,w/size)
    y_apple = random.randint(1,h/size)
    
    run = True
    while run:
        clock.tick(15)
        apple = pg.Rect((x_apple*size)-size, (y_apple*size)-size, size, size)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and movement != 'down':
                    movement = 'up'
                    break
                if event.key == pg.K_DOWN and movement != 'up':
                    movement = 'down'  
                    break         
                if event.key == pg.K_LEFT and movement != 'right':
                    movement = 'left'
                    break
                if event.key == pg.K_RIGHT and movement != 'left':
                    movement = 'right'
                    break
                    
        if snake[0][0].x == apple.x and snake[0][0].y == apple.y:
            x_apple = random.randint(1,w/size)
            y_apple = random.randint(1,h/size)

            snake.append([pg.Rect(
                snake[0][0].x, snake[0][0].y, size, size), 
                pg.Rect(snake[0][1].x + size_config, snake[0][1].y + size_config, size4, size4)])

        follow(snake)
        movements(movement, snake)
        draw(screen, snake, apple)
        pg.display.update()
        
        if collide(snake) or not (-1 < snake[0][0].x < w) or not (-1 < snake[0][0].y < h):
            main()

    pg.quit()

main()
