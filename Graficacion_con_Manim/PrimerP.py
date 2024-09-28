from manim import *

class FirstScene(Scene):
    def construct(self):
        # se crea un cuadrado
        sq = Square()
        # se crea un circulo con opacidad completa
        circ = Circle().set_fill(opacity=1)
        # se transforma el cuadrado en el circulo con una animacion
        self.play(Transform(sq, circ))

        # y se espera hasta que la animacion este completa
        self.wait()