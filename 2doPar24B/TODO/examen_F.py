import numpy as np
import matplotlib.pyplot as plt

# Definir los puntos de la letra A
F = np.array([
    (0, 0, 1),
    (1, 0, 1),
    (1, 2, 1),
    (2, 2, 1),
    (2, 3, 1),
    (1, 3, 1),
    (1, 4, 1),
    (3, 4, 1),
    (3, 5, 1),
    (0, 5, 1),
    (0, 0, 1)
])

# Matrices de transformación
theta = 5 * np.pi / 4  # Ángulo de rotación
matrices = {
    "Identidad": np.eye(3),
    "Reflexión X": np.array([[1., 0, 0], [0, -1., 0], [0., 0., 1.]]),
    "Reflexión Y": np.array([[-1., 0, 0], [0, 1., 0], [0., 0., 1.]]),
    "Rotación": np.array([[np.cos(theta), np.sin(theta), 0],
                          [-np.sin(theta), np.cos(theta), 0],
                          [0, 0, 1]]),
    "Escala": np.array([[3, 0, 0], [0, 3, 0], [0, 0, 1]]),
    "Traslación": np.array([[1, 0, 3], [0, 1, 2], [0, 0, 1]]),
    "Deformación": np.array([[1, 0.5, 0], [0.5, 1, 0], [0, 0, 1]])
}

# Crear subplots
num_transforms = len(matrices)
fig, axes = plt.subplots(2, (num_transforms + 1) // 2, figsize=(15, 10))
axes = axes.flatten()

# Iterar sobre cada transformación y graficarla
for i, (name, matrix) in enumerate(matrices.items()):
    transformed = F @ matrix.T  # Multiplicación de matriz
    axes[i].plot(F[:, 0], F[:, 1], color="blue", label="Original")
    axes[i].plot(transformed[:, 0], transformed[:, 1], color="red", label="Transformada")
    axes[i].set_title(name)
    print(name)
    print(transformed)
    print()
    
    axes[i].set_xticks(np.arange(-5, 10, 1))
    axes[i].set_yticks(np.arange(-5, 10, 1))
    axes[i].set_aspect('equal', adjustable='box')
    axes[i].grid()
    axes[i].legend()

# Ajustar el diseño
plt.tight_layout()
plt.show()
