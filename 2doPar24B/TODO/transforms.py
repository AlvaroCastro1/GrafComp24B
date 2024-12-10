from manim import *

class TransformationText1V1(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY  # Cambia el color de fondo
        texto1 = Text("First text")
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()

class TransformationText1V2(Scene):
    def construct(self):
        self.camera.background_color = RED
        texto1 = Text("First text").to_edge(UP)
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()

class TransformationText2(Scene):
    def construct(self):
        self.camera.background_color = GREEN
        text1 = Text("Function")
        text2 = Text("Derivative")
        text3 = Text("Integral")
        text4 = Text("Transformation")
        self.play(Write(text1))
        self.wait()
        self.play(ReplacementTransform(text1, text2))
        self.wait()
        self.play(ReplacementTransform(text2, text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait()

class CopyTextV1(Scene):
    def construct(self):
        self.camera.background_color = BLUE
        formula = MathTex(
            r"\frac{d}{dx}", "(", "u", "+", "v", ")", "=",
            r"\frac{d}{dx}", "u", "+", r"\frac{d}{dx}", "v"
        ).scale(2)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9])
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10])
        )
        self.wait()

class CopyTextV2(Scene):
    def construct(self):
        self.camera.background_color =YELLOW
        formula = MathTex(
            r"\frac{d}{dx}", "(", "u", "+", "v", ")", "=",
            r"\frac{d}{dx}", "u", "+", r"\frac{d}{dx}", "v"
        ).scale(2)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()

class CopyTextV3(Scene):
    def construct(self):
        self.camera.background_color = ORANGE
        formula = MathTex(
            r"\frac{d}{dx}", "(", "u", "+", "v", ")", "=",
            r"\frac{d}{dx}", "u", "+", r"\frac{d}{dx}", "v"
        ).scale(2)
        formula[8].set_color(RED)
        formula[11].set_color(BLUE)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()

class CopyTextV4(Scene):
    def construct(self):
        formula = MathTex(
            r"\frac{d}{dx}", "(", "u", "+", "v", ")", "=",
            r"\frac{d}{dx}", "u", "+", r"\frac{d}{dx}", "v"
        ).scale(2)
        formula.set_color_by_tex("u", RED)
        formula.set_color_by_tex("v", BLUE)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()

class CopyTwoFormulas1(Scene):
    def construct(self):
        self.camera.background_color = GOLD
        formula1 = MathTex(r"\neg", r"\forall", "x", ":", r"P(x)").scale(2).move_to(2 * UP)
        formula2 = MathTex(r"\exists", "x", ":", r"\neg", r"P(x)").scale(2).move_to(2 * DOWN)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(0, 1, 2, 3, 4), (3, 0, 1, 2, 4)],
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(), formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()

class CopyTwoFormulas2(Scene):
    def construct(self):
        self.camera.background_color = TEAL
        formula1 = MathTex(r"\neg", r"\forall", "x", ":", r"P(x)").scale(2).move_to(2 * UP)
        formula2 = MathTex(r"\exists", "x", ":", r"\neg", r"P(x)").scale(2).move_to(2 * DOWN)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(2, 3, 4), (1, 2, 4)],
            [(0,), (3,)],
            [(1,), (0,)],
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(), formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()

class CopyTwoFormulas2Color(Scene):
    def construct(self):
        self.camera.background_color = GRAY
        formula1 = MathTex(r"\neg", r"\forall", "x", ":", r"P(x)").scale(2).move_to(2 * UP)
        formula2 = MathTex(r"\exists", "x", ":", r"\neg", r"P(x)").scale(2).move_to(2 * DOWN)
        formula1.set_color_by_tex(r"\forall", GREEN)
        formula2.set_color_by_tex(r"\exists", ORANGE)
        formula1.set_color_by_tex(r"\neg", PINK)
        formula2.set_color_by_tex(r"\neg", PINK)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(2, 3, 4), (1, 2, 4)],
            [(0,), (3,)],
            [(1,), (0,)],
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(), formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()

class CopyTwoFormulas3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        formula1 = MathTex(r"\neg", r"\forall", "x", ":", r"P(x)").scale(2).move_to(2 * UP)
        formula2 = MathTex(r"\exists", "x", ":", r"\neg", r"P(x)").scale(2).move_to(2 * DOWN)
        formula1.set_color_by_tex(r"\forall", GREEN)
        formula2.set_color_by_tex(r"\exists", ORANGE)
        formula1.set_color_by_tex(r"\neg", PINK)
        formula2.set_color_by_tex(r"\neg", PINK)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(2, 3, 4), (1, 2, 4)],
            [(0,), (3,)],
            [(1,), (0,)],
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i], formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()

class ChangeTextColorAnimation(Scene):
    def construct(self):
        text = Text("Text").scale(3)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.set_color(YELLOW),
            run_time=2
        )
        self.wait()

class ChangeSizeAnimation(Scene):
    def construct(self):
        self.camera.background_color = PURPLE
        text = Text("Text").scale(2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.scale(3),
            run_time=2
        )
        self.wait()

class MoveText(Scene):
    def construct(self):
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2),
            run_time=2
        )
        self.wait()

class ChangeColorAndSizeAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLUE  # Cambiar el fondo dinámicamente
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2).scale(2).set_color(RED),
            run_time=2
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
        description = Text("transform", font_size=24)
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