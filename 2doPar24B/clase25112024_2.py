from manim import *

COLOR_P = "#3EFC24"

class TextColor(Scene):
    def construct(self):
        text = Tex("A", "B", "C", "D", "E", "F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")  # Hexadecimal color
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)

class FormulaColor1(Scene): 
    def construct(self):
        text = MathTex("x", "=", "{a", "\over", "b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        self.play(Write(text))
        self.wait(2)

class FormulaColor2(Scene): 
    def construct(self): 
        text = MathTex("x", "=", "\\frac{a}{b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3(Scene): 
    def construct(self):
        text = MathTex("\\sqrt{", "\int_{", "a}^", "{b}", "\left(", "\\frac{x}{y}", "\\right)", "dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3Fixed(Scene): 
    def construct(self): 
        text = MathTex("\sqrt{", "\int_", "{a}", "^", "{b}", "\left(", "\\frac{x}{y}", "\\right)", "dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(ORANGE)
        text[5].set_color(PINK)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(GRAY)
        self.play(Write(text))
        self.wait(3)

class FormulaColor3Fixed2(Scene): 
    def construct(self): 
        # Reestructuramos la expresión para asegurarnos de que se compile bien
        text = MathTex(
            r"\sqrt{",  # Inicio de raíz cuadrada
            r"\int_{a}^{b}",  # Integral con límites inferior (a) y superior (b)
            r"\left( \frac{x}{y} \right)",  # Fracción (x/y) entre paréntesis
            r"dx",  # Elemento diferencial
            r"}"  # Fin de la raíz cuadrada
        )

        # Asignar colores a cada parte
        text[0].set_color(RED)      # \sqrt{
        text[1].set_color(BLUE)     # \int_{a}^{b}
        text[2].set_color(GREEN)    # \left( \frac{x}{y} \right)
        text[3].set_color(YELLOW)   # dx
        text[4].set_color(ORANGE)   # }

        # Reproducir la animación
        self.play(Write(text))
        self.wait(3)

class FormulaColor4(Scene): 
    def construct(self): 
        # Reestructuramos la expresión para evitar problemas con LaTeX
        text = MathTex(
            r"\sqrt{",  # Inicio de raíz cuadrada
            r"\int_{a+c}^{b}",  # Integral con límites inferior (a+c) y superior (b)
            r"\left( \frac{x}{y} \right)",  # Fracción (x/y) entre paréntesis
            r"d", "x", r".}"  # Elemento diferencial y finalización de la raíz
        )

        # Asignar colores a cada parte de la fórmula
        text[0].set_color(RED)       # \sqrt{
        text[1].set_color(BLUE)      # \int_{a+c}^{b}
        text[2].set_color(GREEN)     # \left( \frac{x}{y} \right)
        text[3].set_color(YELLOW)    # d
        text[4].set_color(PINK)      # x
        text[5].set_color(ORANGE)    # .}

        # Reproducir la animación
        self.play(Write(text))
        self.wait(3)

class FormulaColor5(Scene): 
    def construct(self): 
        # Reestructuramos la expresión para evitar problemas con LaTeX
        text = MathTex(
            r"\sqrt{",  # Inicio de raíz cuadrada
            r"\int_{a+c}^{b}",  # Integral con límites inferior (a+c) y superior (b)
            r"\left( \frac{x}{y} \right)",  # Fracción (x/y) entre paréntesis
            r"d", "x", r".}"  # Elemento diferencial y finalización de la raíz
        )

        # Asignar colores a cada parte de la fórmula usando un bucle for corregido
        colors = [PURPLE, BLUE, GREEN, YELLOW, PINK, ORANGE]
        for i, color in enumerate(colors):
            text[i].set_color(color)

        # Reproducir la animación
        self.play(Write(text))
        self.wait(3)

class ColorByCharacter(Scene):
    def construct(self):
        text = MathTex("{d", "\over", "d", "x", "}", "\int_", "{a}^", "{", "x", "}", "f(", "t", ")d", "t", "=", "f(", "x", ")")
        text.set_color_by_tex("x", RED)
        self.play(Write(text))
        self.wait(2)

class ColorByCharacterFixed(Scene):
    def construct(self):
        text = MathTex("{d", "\over", "d", "x", "}", "\int_", "{a}^", "{", "x", "}", "f(", "t", ")d", "t", "=", "f(", "x", ")")
        text.set_color_by_tex("x", RED)
        text[6].set_color(RED)
        text[8].set_color(WHITE)
        self.play(Write(text))
        self.wait(2)

class ListFor(Scene): 
    def construct(self):
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in [0, 1, 3, 4]:
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange1(Scene): 
    def construct(self):
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in range(3):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange2(Scene): 
    def construct(self):
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in range(2, 6):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForTwoVariables(Scene): 
    def construct(self):
        text = MathTex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i, color in [(2, RED), (4, PINK)]:
            text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)

class ChangeSize(Scene):
    def construct(self):
        # Definir el objeto MathTex
        text = MathTex(r"\sum_{i=0}^n i=\frac{n(n+1)}{2}")
        self.add(text)  # Añadir el texto a la escena
        self.wait()

        # Escalar el texto con una animación
        self.play(text.animate.scale(2))
        self.wait(2)

class AddAndRemoveText(Scene):
    def construct(self):
        text = Text("Text or object")
        self.wait()
        self.add(text)
        self.wait()
        self.remove(text)
        self.wait()

class FadeText(Scene):
    def construct(self):
        text = Text("Text or object")
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text), run_time=1)
        self.wait()

class FadeTextFromDirection(Scene):
    def construct(self):
        text = Text("Text or object")
        self.play(FadeIn(text, shift=DOWN), run_time=1)
        self.wait()

class GrowObjectFromCenter(Scene):
    def construct(self):
        text = Text("Text or object")
        self.play(GrowFromCenter(text), run_time=1)
        self.wait()

class ShowCreationObject(Scene):
    def construct(self):
        text = Text("Text or object")
        self.play(Create(text), run_time=1)
        self.wait()

class ColoringText(Scene):
    def construct(self):
        text = Text("Text or object")
        self.add(text)
        self.wait(0.5)
        for letter in text:
            self.play(ApplyMethod(letter.set_color, YELLOW), run_time=0.12)
        self.wait(0.5)

class CrossText1(Scene):
    def construct(self):
        # Definir el objeto MathTex
        text = MathTex(r"\sum_{i=1}^{\infty}i", "=", r"-\frac{1}{2}")
        
        # Añadir el texto a la escena
        self.play(Write(text))
        self.wait(0.5)
        
        # Crear un símbolo de tachado sobre la tercera parte del texto
        cross = Cross(text[2])
        cross.set_stroke(color=RED, width=6)
        
        # Añadir el símbolo de tachado a la escena con animación
        self.play(Create(cross))
        self.wait(2)

class CrossText2(Scene):
    def construct(self):
        # Definir el objeto MathTex
        text = MathTex(r"\sum_{i=1}^{\infty}i", "=", r"-\frac{1}{2}")

        # Crear un grupo que contiene el signo de igualdad y el valor incorrecto
        eq = VGroup(text[1], text[2])
        
        # Crear un símbolo de tachado sobre el grupo
        cross = Cross(eq)
        cross.set_stroke(color=RED, width=6)

        # Añadir el texto a la escena
        self.play(Write(text))
        self.wait(0.5)

        # Añadir el símbolo de tachado con animación
        self.play(Create(cross))
        self.wait(2)

class FrameBox1(Scene):
    def construct(self):
        text = MathTex(
            "\hat g(", "f", ")", "=", "\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\pi i", "f", "t}", "dt"
        )
        frame_box = SurroundingRectangle(text[4], buff=0.5 * SMALL_BUFF)
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frame_box))
        self.wait(2)

class FrameBox2(Scene):
    def construct(self):
        text = MathTex(
            "\hat g(", "f", ")", "=", "\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\pi i", "f", "t}", "dt"
        )
        seleccion = VGroup(text[4], text[5], text[6])
        frame_box = SurroundingRectangle(seleccion, buff=0.5 * SMALL_BUFF)
        frame_box.set_stroke(GREEN, 9)
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frame_box))
        self.wait(2)

class BraceText(Scene):
    def construct(self):
        # Definir la expresión con MathTex
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", "+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        
        # Añadir la expresión a la escena
        self.play(Write(text))
        
        # Crear los corchetes y los textos relacionados
        brace_top = Brace(text[1], UP, buff=SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff=SMALL_BUFF)
        
        # Añadir las etiquetas correspondientes para los corchetes
        text_top = brace_top.get_text(r"$g'f$")
        text_bottom = brace_bottom.get_text(r"$f'g$")
        
        # Reproducir las animaciones de los corchetes y las etiquetas
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
        )
        
        # Esperar para mostrar el resultado final
        self.wait()
