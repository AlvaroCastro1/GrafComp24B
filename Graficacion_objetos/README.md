# Notebooks de Graficación en Python

Este repositorio contiene tres notebooks que implementan diferentes métodos para graficar vectores y figuras geométricas utilizando librerías populares en Python, como **Matplotlib** y **Numpy**. A continuación, se ofrece una descripción de cada notebook, los métodos utilizados y una breve explicación de los fragmentos de código más importantes.

## 1. `figuras_plot.ipynb`

Este notebook está enfocado en la creación de figuras geométricas básicas (como círculos, cuadrados y triángulos) utilizando la librería **Matplotlib**.

### Fragmento de Código Clave:

```python
circle = plt.Circle((0.5, 0.5), 0.2, color='blue')  # Crear un círculo
ax.add_patch(circle)  # Añadir el círculo al gráfico
plt.xlim(0, 1)  # Definir límites del eje X
plt.ylim(0, 1)  # Definir límites del eje Y
```

#### Explicación:
- **`plt.Circle()`**: Crea un círculo con centro en `(0.5, 0.5)` y radio de `0.2`.
- **`ax.add_patch()`**: Añade el círculo al gráfico para su representación.
- **`plt.xlim()` y `plt.ylim()`**: Definen los límites de los ejes para asegurar que la figura se vea correctamente.

---

## 2. `suma_vectores_arrow.ipynb`

Este notebook muestra cómo representar la suma de vectores utilizando flechas para representar los vectores.

### Fragmento de Código Clave:

```python
v1 = np.array([1, 2])
v2 = np.array([3, 1])
v3 = v1 + v2  # Suma de vectores

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='g')
```

#### Explicación:
- **`np.array()`**: Se usa para definir los vectores.
- **`plt.quiver()`**: Dibuja las flechas en el gráfico, con origen en `(0,0)` y direcciones definidas por los componentes de los vectores. Los colores (`r`, `b`, `g`) representan cada vector.
- **`v3 = v1 + v2`**: Realiza la suma de los vectores `v1` y `v2`.

### Contenido:
- Representación visual de vectores utilizando flechas.
- Suma de vectores y su representación gráfica.
- Uso de la función `quiver` para graficar flechas.

---

## 3. `vectores_quiver.ipynb`

Este notebook presenta un enfoque similar al anterior, usando la función `quiver` para graficar múltiples vectores al mismo tiempo, con un enfoque en el control de colores y límites de los ejes.

### Fragmento de Código Clave:

```python
v1 = np.array ([1, 2])
v2 = np.array([3, 4])
v3 = np.array([8, 4])

grafvecs([v1, v2, v3], ['blue', 'red', "black"])  # Graficar los vectores
plt.xlim(0, max(v1[0], v2[0], v3[0]))  # Ajustar límites del eje X
plt.ylim(0, max(v1[1], v2[1], v3[1]))  # Ajustar límites del eje Y
```

#### Explicación:
- **`grafvecs([v1, v2, v3], ['blue', 'red', 'black'])`**: Esta función personalizada dibuja los tres vectores `v1`, `v2` y `v3` con los colores correspondientes.
- **`plt.xlim()` y `plt.ylim()`**: Ajustan los límites de los ejes según los valores máximos de los vectores para asegurarse de que todos los vectores sean visibles en el gráfico.

### Contenido:
- Representación de múltiples vectores en un gráfico.
- Control de los colores y los límites de los ejes para mejorar la visualización.
- Uso de la función `quiver` con varias configuraciones.
