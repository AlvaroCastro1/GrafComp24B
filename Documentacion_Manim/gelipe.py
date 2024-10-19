from manim import *

class RobotDesign(Scene):
    def construct(self):
        # Título
        nombre = Text("Gelipe", font_size=55)
        nombre.move_to(ORIGIN + UP * 2)
        self.play(Write(nombre))
        self.wait(1)

        # Crear el cuerpo principal como una elipse
        cuerpo = Ellipse(width=5, height=2, color=BLUE, fill_opacity=1)
        cuerpo.shift(DOWN * 0.5)  # Bajar el cuerpo
        self.play(Create(cuerpo))
        self.wait(1)

        # Crear los ojos
        ojo1 = Polygon([-0.7, -0.1, 0], [-0.2, -0.1, 0], [-0.45, -0.5, 0], color=WHITE, fill_opacity=1)
        ojo2 = Polygon([0.7, -0.1, 0], [0.2, -0.1, 0], [0.45, -0.5, 0], color=WHITE, fill_opacity=1)
        ojo1.shift(LEFT * 0.35 + DOWN * 0.01)  # Ajustar el ojo izquierdo
        ojo2.shift(RIGHT * 0.35 + DOWN * 0.01)  # Ajustar el ojo derecho
        self.play(Create(ojo1), Create(ojo2))
        self.wait(1)

        # Crear los brazos
        brazo1 = RoundedRectangle(width=2, height=0.5, color=BLUE, fill_opacity=1)
        brazo2 = RoundedRectangle(width=2, height=0.5, color=BLUE, fill_opacity=1)

        brazo1.rotate(PI / 8)
        brazo2.rotate(-PI / 8)

        brazo1.shift(LEFT * 3 + DOWN * 1)  # Bajar los brazos
        brazo2.shift(RIGHT * 3 + DOWN * 1)
        self.play(Create(brazo1), Create(brazo2))
        self.wait(1)

        # Crear las piernas
        pierna1 = Square(side_length=0.7, color=BLUE, fill_opacity=1)
        pierna2 = Square(side_length=0.7, color=BLUE, fill_opacity=1)

        pierna1.shift(LEFT * 0.75 + DOWN * 1.7)
        pierna2.shift(RIGHT * 0.75 + DOWN * 1.7)
        self.play(Create(pierna1), Create(pierna2))
        self.wait(1)

        # Crear los pies
        pie1 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=BLUE, fill_opacity=1)
        pie2 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=BLUE, fill_opacity=1)

        pie1.shift(LEFT * 0.75 + DOWN * 2.1)
        pie2.shift(RIGHT * 0.75 + DOWN * 2.1)
        self.play(Create(pie1), Create(pie2))
        self.wait(1)

        # Crear la boca como una flecha curva doble
        flecha_curva_doble = CurvedDoubleArrow(
            start_point=LEFT * 0.8, end_point=RIGHT * 0.8, color=YELLOW, angle=-PI / 2
        )
        flecha_curva_doble.shift(DOWN * 1.2)  # Colocar la flecha curva doble más abajo
        flecha_curva_doble.scale(0.7)  # Ajustar el tamaño de la "boca"
        self.play(Create(flecha_curva_doble))
        self.wait(1)

        # Agrupar pierna1 y pie1 para moverlos juntos
        pierna_y_pie1 = VGroup(pierna1, pie1)

        # Animación para levantar el brazo derecho y mover la pierna y el pie juntos
        punto_fijo_brazo2 = brazo2.get_left()  # Mantener este punto fijo
        punto_fijo_pierna1 = pierna1.get_top()  # Punto fijo para rotar la pierna desde la parte superior
        punto_fijo_boca1 = flecha_curva_doble.get_top()

        # Agrupar las animaciones
        animaciones = AnimationGroup(
            Rotate(brazo2, angle=PI / 3, about_point=punto_fijo_brazo2),
            Rotate(pierna_y_pie1, angle=-PI / 6, about_point=punto_fijo_pierna1),
            Rotate(flecha_curva_doble, angle= 2*PI / 2, about_point=punto_fijo_boca1)  # Girar hacia arriba para sonreír
        )

        self.play(animaciones)
        self.wait(0.5)

        # Regresar a la posición original
        animaciones_invertidas = AnimationGroup(
            Rotate(brazo2, angle=-PI / 3, about_point=punto_fijo_brazo2),
            Rotate(pierna_y_pie1, angle=PI / 6, about_point=punto_fijo_pierna1),
            Rotate(flecha_curva_doble, angle= -2*PI / 2, about_point=punto_fijo_boca1)  # Regresar a la posición original
        )

        self.play(animaciones_invertidas)
        self.wait(3)

