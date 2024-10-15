from manim import *

class WriteStuff(Scene):
    def construct(self):
        # Crear el texto usando set_color_by_t2c para colorear una parte
        example_text = Text("This is some text")
        example_text.set_color_by_t2c({"text": YELLOW})  # Colorear la palabra "text" de amarillo

        # Crear una expresión matemática con los delimitadores correctos
        example_tex = Tex(
            "$\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}$"
        )
        
        # Agrupar ambos objetos y organizarlos
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config.frame_width - 2 * LARGE_BUFF)  # Usar config.frame_width en lugar de FRAME_WIDTH

        # Animaciones
        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()
