from manim import *

class MoveBraces(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY  # Fondo para esta escena
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=",       # 0
            r"f(x)\frac{d}{dx}g(x)",        # 1
            "+",                            # 2
            r"g(x)\frac{d}{dx}f(x)"         # 3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text(r"$g'f$")
        t2 = brace2.get_text(r"$f'g$")
        self.play(GrowFromCenter(brace1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(brace1, brace2), ReplacementTransform(t1, t2))
        self.wait()

class MoveBracesCopy(Scene):
    def construct(self):
        self.camera.background_color = LIGHT_GRAY  # Fondo para esta escena
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", "+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text(r"$g'f$")
        t2 = brace2.get_text(r"$f'g$")
        self.play(GrowFromCenter(brace1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(brace1.copy(), brace2), ReplacementTransform(t1.copy(), t2))
        self.wait()

class MoveFrameBox(Scene):
    def construct(self):
        self.camera.background_color = BLUE_E  # Fondo para esta escena
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", "+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()

class MoveFrameBoxCopy(Scene):
    def construct(self):
        self.camera.background_color = TEAL_E  # Fondo para esta escena
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", "+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1.copy(), framebox2, path_arc=-np.pi))
        self.wait()

class MoveFrameBoxCopy2(Scene):
    def construct(self):
        self.camera.background_color = ORANGE  # Fondo para esta escena
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", "+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        t1 = MathTex(r"g'f").next_to(framebox1, UP, buff=0.1)
        t2 = MathTex(r"f'g").next_to(framebox2, UP, buff=0.1)
        self.play(Create(framebox1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(framebox1.copy(), framebox2), ReplacementTransform(t1.copy(), t2))
        self.wait()

class Arrow1(Scene):
    def construct(self):
        self.camera.background_color = PINK  # Fondo para esta escena
        step1 = Text("Step 1").move_to(LEFT * 2)
        step2 = Text("Step 2")
        arrow = Arrow(LEFT, RIGHT)
        arrow.next_to(step1, RIGHT, buff=0.1)
        step2.next_to(arrow, RIGHT, buff=0.1)
        self.play(Write(step1))
        self.wait()
        self.play(GrowArrow(arrow))
        self.play(Write(step2))
        self.wait()

class Arrow2(Scene):
    def construct(self):
        self.camera.background_color = MAROON  # Fondo para esta escena
        step1 = Text("Step 1").move_to(LEFT * 2 + DOWN * 2)
        step2 = Text("Step 2").move_to(RIGHT * 4 + UP * 2)
        arrow1 = Arrow(step1.get_right(), step2.get_left(), buff=0.1).set_color(RED)
        arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff=0.1).set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait()

class LineAnimation(Scene):
    def construct(self):
        self.camera.background_color = PURPLE  # Fondo para esta escena
        step1 = Text("Step 1").move_to(LEFT * 2 + DOWN * 2)
        step2 = Text("Step 2").move_to(RIGHT * 4 + UP * 2)
        arrow1 = Line(step1.get_right(), step2.get_left(), buff=0.1).set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1).set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()

class DashedLineAnimation(Scene):
    def construct(self):
        self.camera.background_color = LIGHT_BROWN  # Fondo para esta escena
        step1 = Text("Step 1").move_to(LEFT * 2 + DOWN * 2)
        step2 = Text("Step 2").move_to(RIGHT * 4 + UP * 2)
        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff=0.1).set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1).set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()

class LineAnimation2(Scene):
    def construct(self):
        self.camera.background_color = GOLD  # Fondo para esta escena
        step1 = Text("Step 1").move_to(LEFT * 2 + DOWN * 2)
        step2 = Text("Step 2").move_to(RIGHT * 4 + UP * 2)
        # Usa Arrow en lugar de Line para compatibilidad con GrowArrow
        line = Arrow(start=step1.get_right(), end=step2.get_left(), buff=0.1)
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(line))  # Crece la flecha
        self.play(step2.animate.shift(LEFT * 2))
        self.wait()

class LineAnimation3(Scene):
    def construct(self):
        self.camera.background_color = GREEN  # Fondo para esta escena
        step1 = Text("Step 1").move_to(LEFT * 2 + DOWN * 2)
        step2 = Text("Step 2").move_to(RIGHT * 4 + UP * 2)
        step3 = step2.copy().next_to(step2, LEFT * 2)
        
        # Cambia Line por Arrow
        line = Arrow(start=step1.get_right(), end=step2.get_left(), buff=0.1)
        line_copy = Arrow(start=step1.get_right(), end=step3.get_bottom(), buff=0.1)

        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(line))  # Usa GrowArrow con Arrow
        self.play(
            ReplacementTransform(step2, step3),
            ReplacementTransform(line, line_copy)
        )
        self.wait()

class Alvaro(Scene):
    def construct(self):
        # Título principal
        title = Text("ALVARO JESUS CASTRO PIZAÑA", font_size=36, weight=BOLD)
        title.to_edge(UP)  # Mover el título a la parte superior

        # Subtítulo
        subtitle = Text("2125698", font_size=28, slant=ITALIC)
        subtitle.next_to(title, DOWN)  # Colocar debajo del título

        # Descripción del contenido
        description = Text("Visual Tool", font_size=24)
        description.next_to(subtitle, DOWN, buff=0.5)  # Colocar debajo del subtítulo

        # Animaciones
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(Write(description))
        self.wait(2)

class ZClosingScene(Scene):
    def construct(self):
        # Título principal
        title = Text("ALVARO JESUS CASTRO PIZAÑA", font_size=36, weight=BOLD)
        title.to_edge(UP)  # Mover el título a la parte superior

        # Subtítulo
        subtitle = Text("GRAFICACIÓN COMPUTACIONAL", font_size=28, slant=ITALIC)
        subtitle.next_to(title, DOWN)  # Colocar debajo del título

        # Descripción del contenido
        description = Text("Periodo: 2024b", font_size=24)
        description.next_to(subtitle, DOWN, buff=0.5)  # Colocar debajo del subtítulo

        # Animaciones
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(Write(description))
        self.wait(2)