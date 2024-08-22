#2do. Ejemplo
from manim import *

class SecondScene(Scene):
    def construct(self):
        # se crea una expresion con MathTex
        text = MathTex("x^2")

        # y se añade a la escena para que aparezca
        self.add(text)