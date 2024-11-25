from manim import *

class Ejemplo(Scene):
    def construct(self):
      
# ejemplo1 
        # vectores a y b
        vector_a = Arrow(start=ORIGIN, end=4/4 * RIGHT + -1/4 * UP, color=RED, buff=0)
        vector_b = Arrow(start=ORIGIN, end=2/4 * RIGHT + 8/4 * UP, color=GREEN, buff=0)

        # nombre de cada vector
        nombre_a = Text("a = (4, -1)").scale(0.5)
        nombre_a.next_to(vector_a, DOWN)
        nombre_b = Text("b = (2, 8)").scale(0.5)
        nombre_b.next_to(vector_b, RIGHT)
        
        # formula
        formula = MathTex("a_1 \\cdot b_1 + a_2 \\cdot b_2 = 0").scale(0.7)
        formula.move_to(3 * LEFT + 2 * UP)
        resultado = MathTex("4 \\cdot 2 + (-1) \\cdot 8 = 0").scale(0.7)
        resultado.next_to(formula, DOWN)
        
        # animaciones
        self.play(Write(formula))
        self.play(Write(resultado))

        self.play(Create(vector_a), Write(nombre_a))
        self.play(Create(vector_b), Write(nombre_b))

        # son ortogonales
        texto = Text("ortogonales hay 90° entre los vectores").to_edge(DOWN).scale(0.8) 
        self.play(Write(texto))
        self.wait(2)

        # desvanecer
        self.play(FadeOut(vector_a), FadeOut(vector_b), FadeOut(nombre_a), FadeOut(nombre_b), FadeOut(formula), FadeOut(resultado), FadeOut(texto))

        
        
# ejemplo2
        # vectores a y b
        vector_a = Arrow(start=ORIGIN, end=6/6 * RIGHT + -18/6 * UP, color=WHITE, buff=0)
        vector_b = Arrow(start=ORIGIN, end=-4/6 * RIGHT + 12/6 * UP, color=GREEN, buff=0)

        nombre_a = Text("a = (6, -18)").scale(0.5)
        nombre_a.next_to(vector_a, DOWN)
        nombre_b = Text("b = (-4, 12)").scale(0.5)
        nombre_b.next_to(vector_b, RIGHT)

        # animaciones
        self.play(Create(vector_a), Write(nombre_a))
        self.play(Create(vector_b), Write(nombre_b))

        # formula y el resultado
        formula = MathTex("\\frac{a_1}{b_1} = \\frac{a_2}{b_2}").scale(0.7)
        formula.move_to(3 * LEFT + 2 * UP)
        resultado = MathTex("\\frac{6}{-4} = \\frac{-18}{12}").scale(0.7)
        resultado.next_to(formula, DOWN)
        igualdad = MathTex("1.5 = 1.5").scale(0.7)
        igualdad.next_to(resultado, DOWN)

        # mostrar la formula y el resultado
        self.play(Write(formula))
        self.play(Write(resultado))
        self.play(Write(igualdad))

        texto = Text("paralelos pues sus coordenadas son proporcionales").to_edge(UP).scale(0.5) 
        self.play(Write(texto))
        self.wait(2)

        # Desvanecer todo
        self.play(FadeOut(vector_a), FadeOut(vector_b), FadeOut(nombre_a), FadeOut(nombre_b), FadeOut(texto))
 