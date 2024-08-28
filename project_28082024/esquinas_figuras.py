from manim import *

class SquareAndCircleCorners(Scene):
    def construct(self):
        # Crear figuras
        circulo1 = Circle()
        circulo1.set_fill(RED, opacity=0.7)

        circulo2 = Circle()
        circulo2.set_fill(WHITE, opacity=0.7)

        cuadrado1 = Square()
        cuadrado1.set_fill(BLUE_D, opacity=0.7)

        cuadrado2 = Square()
        cuadrado2.set_fill(PURPLE, opacity=0.7)

        circulo1.to_corner(UR)
        cuadrado1.to_corner(UL)

        circulo2.to_corner(DL)
        cuadrado2.to_corner(DR)

        self.play(Create(circulo1), Create(circulo2), Create(cuadrado1), Create(cuadrado2))
