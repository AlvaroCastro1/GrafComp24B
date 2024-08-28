from manim import *

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()  # crear un cuadrado
        square.rotate(PI)  # rotar para que coincida mejor con la transformación

        self.play(Create(circle))  # animar la creación del círculo
        self.play(Transform(circle, square))  # transformar el círculo en el cuadrado
        self.play(FadeOut(circle))  # desvanecer la figura final (cuadrado)

