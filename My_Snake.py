import pygame

# Definir las dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Inicializar Pygame
pygame.init()

# Crear la ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Señal PQRS")

# Definir los colores que se utilizarán
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definir las coordenadas iniciales para dibujar la señal
x, y = 0, HEIGHT/2

# Definir la amplitud y la frecuencia de la señal
amplitude = 50
frequency = 0.05

# Pedir al usuario que ingrese los valores PQRS
p = input("Ingrese el valor de P: ")
q = input("Ingrese el valor de Q: ")
r = input("Ingrese el valor de R: ")
s = input("Ingrese el valor de S: ")

# Crear una lista con los valores de la señal PQRS
signal = [int(p), int(q), int(r), int(s)]

# Dibujar la señal en la ventana
window.fill(WHITE)
pygame.draw.line(window, BLACK, (0, HEIGHT/2), (WIDTH, HEIGHT/2), 2)
for value in signal:
    x += 10
    y = HEIGHT/2 - value * amplitude
    pygame.draw.circle(window, RED, (int(x), int(y)), 5)

# Actualizar la ventana
pygame.display.update()

# Esperar a que el usuario cierre la ventana
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Salir de Pygame
pygame.quit()
