# Animaciones con Manim

## Ejecución


```bash
manim -pql nombre_del_script.py NombreDeLaClase
```

Donde:
- `nombre_del_script.py` es el archivo con el código.
- `NombreDeLaClase` es el nombre de la clase que deseas ejecutar.
- `-pql` se refiere a la calidad baja de renderizado (puedes usar `-pqh` para alta calidad).

---

## Clases y Escenas

### 1. `CreateCircle`

```python
circle = Circle()  # Crea un círculo
circle.set_fill(BLUE_A, opacity=3.0)  # Aplica color y opacidad
self.play(Create(circle))  # Anima la creación del círculo
```

#### Explicación:
- **`Circle()`**: Crea un círculo con las propiedades predeterminadas de Manim.
- **`set_fill(BLUE_A, opacity=3.0)`**: Establece el color del círculo (en este caso, azul). La opacidad suele estar en un rango de 0 (transparente) a 1 (opaco), por lo que `3.0` es un valor que no tendrá el efecto esperado.
- **`self.play(Create(circle))`**: Muestra la animación de creación del círculo.

---

### 2. `SquareToCircle`

```python
square = Square()  # Crea un cuadrado
square.rotate(PI / 2)  # Rota el cuadrado 90 grados
self.play(Transform(square, circle))  # Transforma el cuadrado en círculo
```

#### Explicación:
- **`Square()`**: Crea un cuadrado.
- **`rotate(PI / 2)`**: Rota el cuadrado 90 grados (`PI/2` radianes).
- **`Transform(square, circle)`**: Transforma el cuadrado en un círculo con una animación suave.

---

### 3. `CircleToSquare`

```python
circle = Circle()  # Crea un círculo
square = Square()  # Crea un cuadrado
square.rotate(PI)  # Rota el cuadrado 180 grados
self.play(Transform(circle, square))  # Transforma el círculo en un cuadrado
```

#### Explicación:
- **`rotate(PI)`**: Rota el cuadrado 180 grados (`PI` radianes) para alinearlo mejor antes de la transformación.
- **`Transform(circle, square)`**: La animación transforma el círculo en el cuadrado.

---

### 4. `SquareAndCircle`

```python
square.next_to(circle, RIGHT, buff=0.5)  # Coloca el cuadrado a la derecha del círculo
self.play(Create(circle), Create(square))  # Muestra ambas figuras simultáneamente
```

#### Explicación:
- **`next_to(circle, RIGHT, buff=0.5)`**: Coloca el cuadrado a la derecha del círculo, dejando un espacio de `0.5` unidades.
- **`Create()`**: Anima la creación de las dos figuras.

---

### 5. Variaciones de `SquareAndCircle`

```python
square.next_to(circle, DOWN, buff=0.5)  # Posiciona el cuadrado debajo del círculo
square.next_to(circle, UP, buff=0.5)    # Posiciona el cuadrado encima del círculo
square.next_to(circle, LEFT, buff=0.5)  # Posiciona el cuadrado a la izquierda del círculo
```

#### Explicación:
- Las posiciones del cuadrado cambian en función de la dirección (arriba, abajo, izquierda) respecto al círculo usando `next_to`.

---

### 6. `SquareAndCircleCorners`

```python
circulo1.to_corner(UR)  # Coloca el círculo en la esquina superior derecha
cuadrado1.to_corner(UL)  # Coloca el cuadrado en la esquina superior izquierda
```

#### Explicación:
- **`to_corner(UR)`**: Coloca una figura en la esquina superior derecha de la pantalla.
- **`to_corner(UL)`**: Coloca una figura en la esquina superior izquierda.
- También se usan **`DL`** (esquina inferior izquierda) y **`DR`** (esquina inferior derecha) para otras figuras.

---

## Notas Adicionales

- **Opacidad**: Para obtener el efecto esperado, la opacidad debe estar en el rango de 0 (totalmente transparente) a 1 (completamente opaco).
- **Rotación**: La rotación se mide en radianes. Por ejemplo, `PI/2` equivale a 90 grados y `PI` a 180 grados.