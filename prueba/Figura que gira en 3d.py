"""import pygame
import numpy as np

# Inicializamos Pygame
pygame.init()

# Establecemos el tamaño de la ventana
screen = pygame.display.set_mode((400, 400))

# Creamos una matriz de transformación de rotación para el cubo
rotation_matrix = np.array([
    [np.cos(np.pi/4), -np.sin(np.pi/4), 0],
    [np.sin(np.pi/4), np.cos(np.pi/4), 0],
    [0, 0, 1]
])

# Creamos una lista de puntos para dibujar el cubo
points = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Creamos una lista de caras para conectar los puntos
faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [2, 3, 7, 6],
    [1, 2, 6, 5],
    [0, 3, 7, 4]
]

# Dibujamos el cubo
while True:
    # Limpiamos la pantalla
    screen.fill((255, 255, 255))

    # Aplicamos la transformación de rotación a los puntos
    rotated_points = [np.matmul(point, rotation_matrix) for point in points]

    # Dibujamos cada cara del cubo
    for face in faces:
        # Obtenemos los puntos de la cara
        face_points = [rotated_points[i] for i in face]

        # Dibujamos la cara
        pygame.draw.polygon(screen, (0, 0, 0), face_points)

    # Actualizamos la pantalla
    pygame.display.flip()"""




