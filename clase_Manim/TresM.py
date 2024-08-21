#3er. Ejemplo
from manim import *

"""
https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html

fracciones -> \frac{}{}
raiz cuadrada -> \sqrt{}
+/- ->\pm 
"""

class ThirdScene(Scene):
    def construct(self):
        text = MathTex(r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        self.add(text)