from manim import *

class MiGelipe_en_bosque(Scene):
    def construct(self):
        COLOR_GELIPE = RED # color principal de gelipe
        
        # Crear un cielo azul de fondo cubriendo toda la pantalla
        cielo = Rectangle(width=config.frame_width, height=config.frame_height).set_fill(BLUE, opacity=1)
        cielo.to_edge(UP)  # Posicionar el cielo en la parte superior de la pantalla
        self.add(cielo)
        
        # Crear una pradera verde como el piso en la parte inferior
        pradera = Rectangle(width=config.frame_width, height=3).set_fill(GREEN, opacity=1)
        pradera.to_edge(DOWN)  # Posicionar la pradera en la parte inferior de la pantalla
        self.add(pradera)

        # Crear el sol como un círculo amarillo con borde naranja en la esquina superior derecha
        sol = Circle(radius=0.6).set_fill(YELLOW, opacity=1).set_stroke(color=ORANGE, width=4)
        sol.move_to(UP * 3.5 + RIGHT * 5)  # Colocar el sol en la esquina superior derecha
        self.add(sol)

        # Crear un árbol (tronco marrón y follaje verde)
        tronco = Rectangle(width=0.3, height=1.5).set_fill(DARK_BROWN, opacity=1)
        tronco.move_to(DOWN * 1.5 + LEFT * 2)  # Posicionar el tronco hacia la izquierda y abajo
        follaje = Circle(radius=1).set_fill(GREEN, opacity=1)
        follaje.move_to(tronco.get_top() + UP * 0.5)  # Posicionar el follaje encima del tronco
        self.add(tronco, follaje)

        # Crear un camino de piedras (óvalos grises) a lo largo de la pradera
        piedra_color = GRAY
        for i in range(6):
            piedra = Ellipse(width=0.5, height=0.2).set_fill(piedra_color, opacity=1)
            piedra.move_to(DOWN * (1 + 0.5 * i) + LEFT * (0.5 * i))  # Colocar las piedras en diagonal
            self.add(piedra)
        
        # Crear nubes blancas en el cielo (óvalos blancos)
        for i in range(3):
            nube = Ellipse(width=2, height=0.7).set_fill(WHITE, opacity=0.8)
            nube.move_to(UP * (3 - i) + LEFT * (5 - i * 2))  # Colocar las nubes en diferentes posiciones en el cielo
            self.add(nube)
        
        #--------------------------------------------------------------------------------------#
        # Creación de Gelipe, el robot
        
        # Crear el cuerpo principal de Gelipe como una elipse roja
        cuerpo = Ellipse(width=5, height=2, color=COLOR_GELIPE, fill_opacity=1)
        cuerpo.shift(DOWN * 0.5)  # Bajar el cuerpo hacia abajo en la escena

        # Crear los ojos de Gelipe como triángulos blancos
        ojo1 = Polygon([-0.7, -0.1, 0], [-0.2, -0.1, 0], [-0.45, -0.5, 0], color=WHITE, fill_opacity=1)  # Ojo izquierdo
        ojo2 = Polygon([0.7, -0.1, 0], [0.2, -0.1, 0], [0.45, -0.5, 0], color=WHITE, fill_opacity=1)  # Ojo derecho
        ojo1.shift(LEFT * 0.35 + DOWN * 0.01)  # Ajustar el ojo izquierdo
        ojo2.shift(RIGHT * 0.35 + DOWN * 0.01)  # Ajustar el ojo derecho

        # Crear los brazos como rectángulos rojos
        brazo1 = RoundedRectangle(width=2, height=0.5, color=COLOR_GELIPE, fill_opacity=1)
        brazo2 = RoundedRectangle(width=2, height=0.5, color=COLOR_GELIPE, fill_opacity=1)
        brazo1.rotate(PI / 8)  # Rotar el brazo izquierdo hacia arriba
        brazo2.rotate(-PI / 8)  # Rotar el brazo derecho hacia abajo
        brazo1.shift(LEFT * 3 + DOWN * 1)  # Posicionar el brazo izquierdo
        brazo2.shift(RIGHT * 3 + DOWN * 1)  # Posicionar el brazo derecho

        # Crear las piernas como cuadrados rojos
        pierna1 = Square(side_length=0.7, color=COLOR_GELIPE, fill_opacity=1)
        pierna2 = Square(side_length=0.7, color=COLOR_GELIPE, fill_opacity=1)
        pierna1.shift(LEFT * 0.75 + DOWN * 1.7)  # Posicionar la pierna izquierda
        pierna2.shift(RIGHT * 0.75 + DOWN * 1.7)  # Posicionar la pierna derecha

        # Crear los pies como triángulos rojos
        pie1 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=COLOR_GELIPE, fill_opacity=1)
        pie2 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=COLOR_GELIPE, fill_opacity=1)
        pie1.shift(LEFT * 0.75 + DOWN * 2.1)  # Posicionar el pie izquierdo
        pie2.shift(RIGHT * 0.75 + DOWN * 2.1)  # Posicionar el pie derecho

        # Crear la boca de Gelipe como una flecha curva doble amarilla
        flecha_curva_doble = CurvedDoubleArrow(
            start_point=LEFT * 0.8, end_point=RIGHT * 0.8, color=YELLOW, angle=-PI / 2
        )
        flecha_curva_doble.shift(DOWN * 1.2)  # Colocar la boca más abajo
        flecha_curva_doble.scale(0.7)  # Ajustar el tamaño de la boca

        # Agrupar todas las partes de Gelipe para tratarlas como una unidad
        gelipe = VGroup(cuerpo, ojo1, ojo2, brazo1, brazo2, pierna1, pierna2, pie1, pie2, flecha_curva_doble)
        
        # COLOR_GELIPEucir el tamaño de Gelipe a la mitad
        gelipe.scale(0.5)
        
        # Mover Gelipe hacia la derecha
        gelipe.shift(RIGHT * 3)

        # Añadir a Gelipe a la escena
        self.add(gelipe)
        self.wait(1)

        # Animación para levantar el brazo derecho y mover la pierna izquierda junto con el pie
        pierna_y_pie1 = VGroup(pierna1, pie1)  # Agrupar la pierna izquierda y el pie para moverlos juntos
        punto_fijo_brazo2 = brazo2.get_left()  # Punto fijo para levantar el brazo derecho
        punto_fijo_pierna1 = pierna1.get_top()  # Punto fijo para rotar la pierna izquierda
        punto_fijo_boca1 = flecha_curva_doble.get_top()  # Punto fijo para rotar la boca (sonrisa)

        # Definir las animaciones para sonreír y levantar el brazo y la pierna
        animaciones = AnimationGroup(
            Rotate(brazo2, angle=PI / 3, about_point=punto_fijo_brazo2),  # Levantar el brazo derecho
            Rotate(pierna_y_pie1, angle=-PI / 6, about_point=punto_fijo_pierna1),  # Mover la pierna izquierda
            Rotate(flecha_curva_doble, angle=2 * PI / 2, about_point=punto_fijo_boca1)  # Sonreír
        )
        self.play(animaciones)
        self.wait(1)

        # Animación para regresar a la posición original
        animaciones_invertidas = AnimationGroup(
            Rotate(brazo2, angle=-PI / 3, about_point=punto_fijo_brazo2),  # Bajar el brazo derecho
            Rotate(pierna_y_pie1, angle=PI / 6, about_point=punto_fijo_pierna1),  # Mover la pierna izquierda de vuelta
            Rotate(flecha_curva_doble, angle=-2 * PI / 2, about_point=punto_fijo_boca1)  # Regresar la boca a la posición original
        )
        self.play(animaciones_invertidas)
        self.wait(2)

        # Pausa final para visualizar la escena antes de terminar
        self.wait()
