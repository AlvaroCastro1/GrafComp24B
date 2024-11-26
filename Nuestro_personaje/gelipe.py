from manim import *

class MiGelipe(Scene):
    def construct(self):
        # color principal de Gelipe
        color_gelipe = BLUE
        
        # Título de la escena
        nombre = Text("Gelipe", font_size=55)  # Crear un texto con el nombre "Gelipe"
        nombre.move_to(ORIGIN + UP * 2)  # Posicionar el texto en la parte superior de la escena
        self.play(Write(nombre))  # Animar la escritura del texto en la pantalla
        self.wait(1)

        # Crear el cuerpo principal de Gelipe como una elipse
        cuerpo = Ellipse(width=5, height=2, color=color_gelipe, fill_opacity=1)  # Crear el cuerpo
        cuerpo.shift(DOWN * 0.5)  # Bajar el cuerpo un poco en la pantalla
        self.play(Create(cuerpo))  # Mostrar la creación del cuerpo
        self.wait(1)

        # Crear los ojos de Gelipe (lista con vertices)
        ojo1 = Polygon([-0.7, -0.1, 0], [-0.2, -0.1, 0], [-0.45, -0.5, 0], color=WHITE, fill_opacity=1)  # Ojo izquierdo
        ojo2 = Polygon([0.7, -0.1, 0], [0.2, -0.1, 0], [0.45, -0.5, 0], color=WHITE, fill_opacity=1)  # Ojo derecho
        ojo1.shift(LEFT * 0.35 + DOWN * 0.01)  # Ajustar la posición del ojo izquierdo
        ojo2.shift(RIGHT * 0.35 + DOWN * 0.01)  # Ajustar la posición del ojo derecho
        self.play(Create(ojo1), Create(ojo2))  # Mostrar los ojos
        self.wait(1)

        # Crear los brazos de Gelipe
        brazo1 = RoundedRectangle(width=2, height=0.5, color=color_gelipe, fill_opacity=1)  # Brazo izquierdo
        brazo2 = RoundedRectangle(width=2, height=0.5, color=color_gelipe, fill_opacity=1)  # Brazo derecho

        brazo1.rotate(PI / 8)  # Rotar el brazo izquierdo ligeramente
        brazo2.rotate(-PI / 8)  # Rotar el brazo derecho ligeramente

        brazo1.shift(LEFT * 3 + DOWN * 1)  # Mover el brazo izquierdo hacia la izquierda y hacia abajo
        brazo2.shift(RIGHT * 3 + DOWN * 1)  # Mover el brazo derecho hacia la derecha y hacia abajo
        self.play(Create(brazo1), Create(brazo2))  # Mostrar los brazos
        self.wait(1)

        # Crear las piernas de Gelipe
        pierna1 = Square(side_length=0.7, color=color_gelipe, fill_opacity=1)  # Pierna izquierda
        pierna2 = Square(side_length=0.7, color=color_gelipe, fill_opacity=1)  # Pierna derecha

        pierna1.shift(LEFT * 0.75 + DOWN * 1.7)  # Ajustar la posición de la pierna izquierda
        pierna2.shift(RIGHT * 0.75 + DOWN * 1.7)  # Ajustar la posición de la pierna derecha
        self.play(Create(pierna1), Create(pierna2))  # Mostrar las piernas
        self.wait(1)

        # Crear los pies de Gelipe
        pie1 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=color_gelipe, fill_opacity=1)  # Pie izquierdo
        pie2 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=color_gelipe, fill_opacity=1)  # Pie derecho

        pie1.shift(LEFT * 0.75 + DOWN * 2.1)  # Ajustar la posición del pie izquierdo
        pie2.shift(RIGHT * 0.75 + DOWN * 2.1)  # Ajustar la posición del pie derecho
        self.play(Create(pie1), Create(pie2))  # Mostrar los pies
        self.wait(1)

        # Crear la boca como una flecha curva doble (simulando una sonrisa)
        flecha_curva_doble = CurvedDoubleArrow(
            start_point=LEFT * 0.8, end_point=RIGHT * 0.8, color=YELLOW, angle=-PI / 2
        )
        flecha_curva_doble.shift(DOWN * 1.2)  # Colocar la flecha curva doble más abajo (posición de la boca)
        flecha_curva_doble.scale(0.7)  # Escalar la flecha para que sea del tamaño adecuado
        self.play(Create(flecha_curva_doble))  # Mostrar la "boca"
        self.wait(1)

        # Agrupar pierna1 y pie1 para moverlos juntos
        pierna_y_pie1 = VGroup(pierna1, pie1)  # Agrupar pierna y pie izquierdo para animarlos juntos

        # Animación para levantar el brazo derecho y mover la pierna y el pie juntos
        punto_fijo_brazo2 = brazo2.get_left()  # Mantener el extremo izquierdo del brazo derecho fijo
        punto_fijo_pierna1 = pierna1.get_top()  # Mantener la parte superior de la pierna izquierda como punto de rotación
        punto_fijo_boca1 = flecha_curva_doble.get_top()  # Mantener la parte superior de la boca como punto de rotación

        # Agrupar las animaciones de rotación
        animaciones = AnimationGroup(
            Rotate(brazo2, angle=PI / 3, about_point=punto_fijo_brazo2),  # Levantar el brazo derecho
            Rotate(pierna_y_pie1, angle=-PI / 6, about_point=punto_fijo_pierna1),  # Mover la pierna izquierda
            Rotate(flecha_curva_doble, angle=2*PI / 2, about_point=punto_fijo_boca1)  # Hacer que la boca sonría
        )

        self.play(animaciones)  # Ejecutar todas las animaciones al mismo tiempo
        self.wait(0.5)

        # Regresar a la posición original
        animaciones_invertidas = AnimationGroup(
            Rotate(brazo2, angle=-PI / 3, about_point=punto_fijo_brazo2),  # Bajar el brazo derecho
            Rotate(pierna_y_pie1, angle=PI / 6, about_point=punto_fijo_pierna1),  # Regresar la pierna izquierda
            Rotate(flecha_curva_doble, angle=-2*PI / 2, about_point=punto_fijo_boca1)  # Regresar la boca a su posición original
        )

        self.play(animaciones_invertidas)  # Ejecutar las animaciones para regresar a la posición original
        self.wait(3)  # Esperar al final de la animación
