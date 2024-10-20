from manim import *

class LaboratorioConPisoPerspectiva(Scene):
    def construct(self):
        # Tamaño de cada azulejo
        tile_size = 0.5
        num_tiles_x = int(config.frame_width / tile_size) + 10  # Aumentar número de azulejos en X para cubrir el ancho
        num_tiles_y = 6  # Número de filas de azulejos

        # Crear el piso de azulejos intercalados
        tiles = VGroup()
        for i in range(num_tiles_x):
            for j in range(num_tiles_y):
                color = BLUE if (i + j) % 2 == 0 else WHITE
                tile = Square(side_length=tile_size).set_fill(color, opacity=1)
                tile.set_stroke(GRAY, width=0.5)  # Borde del azulejo
                tile.move_to(np.array([
                    i * tile_size - config.frame_width / 2 + tile_size / 2,
                    j * tile_size - config.frame_height / 2 + tile_size / 2 - 1,  # Mover el piso más abajo
                    0
                ]))
                tiles.add(tile)

        # Aplicar perspectiva inclinada
        perspective_matrix = [[1, 0.5, 0], [0, 1, 0], [0, 0, 1]]
        tiles.apply_matrix(perspective_matrix)
        self.add(tiles)

        # Fondo del laboratorio (pared)
        pared = Rectangle(width=config.frame_width, height=5.5).set_fill(GRAY, opacity=0.8)
        pared.to_edge(UP)  # Coloca la pared en la parte superior
        self.add(pared)

        # Pata izquierda
        pata_izquierda = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_izquierda.move_to(DOWN * 2 + RIGHT * 4.2)  # Ajusta la posición de la pata izquierda
        self.add(pata_izquierda)

        # Pata derecha
        pata_derecha = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_derecha.move_to(DOWN * 2 + RIGHT * 5.8)  # Ajusta la posición de la pata derecha
        self.add(pata_derecha)

        # Escritorio
        escritorio = Rectangle(width=3, height=0.4).set_fill(DARK_BROWN, opacity=1)
        escritorio.move_to(DOWN * 1.5 + RIGHT * 5)  # Coloca el escritorio en la parte inferior central
        self.add(escritorio)

        # Monitor (computadora)
        monitor = Rectangle(width=1.2, height=0.8).set_fill(BLUE_E, opacity=0.9)
        monitor.move_to(escritorio.get_top() + UP * 0.6)  # Encima del escritorio
        self.add(monitor)

        # Base del monitor (la torre o soporte)
        base_monitor = Rectangle(width=0.2, height=0.3).set_fill(GRAY, opacity=1)
        base_monitor.next_to(monitor, DOWN, buff=0.05)
        self.add(base_monitor)

        # Ventana en la pared
        ventana = Rectangle(width=3, height=1.5).set_fill(WHITE, opacity=0.5)
        ventana.to_edge(UP).shift(DOWN * 0.5)  # Ventana en la parte superior de la pared
        self.add(ventana)

        # Detalles en la ventana (rejilla)
        lineas_verticales = VGroup(
            Line(ventana.get_top(), ventana.get_bottom()).shift(LEFT * 1),
            Line(ventana.get_top(), ventana.get_bottom()).shift(RIGHT * 1)
        )
        lineas_horizontales = VGroup(
            Line(ventana.get_left(), ventana.get_right()).shift(UP * 0.5),
            Line(ventana.get_left(), ventana.get_right()).shift(DOWN * 0.5)
        )
        self.add(lineas_verticales, lineas_horizontales)

        # Librero (estructura del librero)
        estante_principal = Rectangle(width=1.2, height=3.5).set_fill(DARK_BROWN, opacity=1)
        estante_principal.to_edge(LEFT).shift(DOWN * 0.5)  # Colocar en el lado izquierdo
        self.add(estante_principal)

        # Crear los estantes usando un bucle for
        for i in range(5):  # 5 estantes
            estante = Line(start=LEFT, end=RIGHT, color=WHITE, stroke_width=4).set_length(1.1)
            estante.move_to(estante_principal.get_top() + DOWN * (0.3 + 0.6 * i))  # Ajuste de la posición para cada estante
            self.add(estante)

        # Libros (rectángulos de colores que representan libros en los estantes)
        libros = []
        colores = [RED, BLUE, GREEN, YELLOW]
        for i in range(4):  # Cuatro estantes
            for j in range(3):  # Tres libros por estante
                libro = Rectangle(width=0.15, height=0.5).set_fill(colores[j % len(colores)], opacity=1)
                libro.move_to(estante_principal.get_top() + DOWN * (0.6 * (i + 1)) + RIGHT * (0.35 * (j - 1)))
                libros.append(libro)

        # Añadir los libros a la escena
        self.add(*libros)


        # Esperar antes de finalizar la escena
        self.wait(5)


class LabWithNewDesk(Scene):
    def construct(self):
        # Crear el escritorio nuevo
        # Parte superior del escritorio
        tabla = Rectangle(width=6, height=0.6, fill_color=RED_D, fill_opacity=1, stroke_color=BLACK)
        tabla.move_to(DOWN * 1.5)  # Coloca el escritorio en la parte inferior central
        
        # Patas del escritorio
        pata_izquierda = Rectangle(width=0.6, height=2, fill_color=RED_D, fill_opacity=1, stroke_color=BLACK)
        pata_izquierda.next_to(tabla, DOWN, buff=0)
        pata_derecha = pata_izquierda.copy().shift(RIGHT * 3.5)

        # Monitor en el escritorio
        monitor = Rectangle(width=2.5, height=1.5, fill_color=LIGHT_BROWN, fill_opacity=1, stroke_color=BLACK)
        marco_monitor = SurroundingRectangle(monitor, color=BLACK, buff=0.1)
        monitor.next_to(pata_derecha, UP, buff=0.2)

        # Añadir todas las partes del escritorio a la escena
        self.add(tabla, pata_izquierda, pata_derecha, monitor, marco_monitor)

        # Ajustar el fondo y el escritorio
        self.wait()
