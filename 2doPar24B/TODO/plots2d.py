from manim import *

class PlotGraph(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY  # Fondo único para esta escena

        # Configuración de los ejes
        axes = Axes(
            x_range=[4, 7, 0.5],
            y_range=[20, 50, 5],
            axis_config={"include_numbers": True, "color": BLUE},
        ).shift(3 * DOWN + 6 * LEFT)

        # Etiquetas para los ejes
        axes.x_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Función y gráfica
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[5, 7])

        # Añadir al escenario
        self.play(Create(axes), Create(graph))
        self.wait()


class Plot1(Scene):
    def construct(self):
        self.camera.background_color = LIGHT_GRAY  # Fondo único para esta escena

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 5],
            axis_config={"include_numbers": True, "color": BLUE},
        )

        # Función y gráfica
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])

        # Añadir al escenario
        self.play(Create(axes), Create(graph))
        self.wait()


class Plot1v2(Scene):
    def construct(self):
        self.camera.background_color = TEAL  # Fondo único para esta escena

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 5],
            axis_config={"include_numbers": True, "color": BLUE},
        )

        # Función y gráfica
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])

        # Añadir al escenario
        self.play(Create(axes), Create(graph))
        self.wait()


class Plot2(Scene):
    def construct(self):
        self.camera.background_color = ORANGE  # Fondo único para esta escena

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[20, 50, 5],
            axis_config={"include_numbers": True, "color": BLUE},
        ).add_coordinates()

        # Función y gráfica
        graph = axes.plot(lambda x: x**2, color=GREEN)

        # Añadir al escenario
        self.play(Create(axes), Create(graph))
        self.wait()


class PlotSinCos(Scene):
    def construct(self):
        self.camera.background_color = PURPLE  # Fondo único para esta escena

        # Configuración de los ejes
        axes = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_numbers": True},
        )

        # Gráficas
        plot_sin = axes.plot(lambda x: np.sin(x), color=GREEN, x_range=[-4, 4])
        plot_cos = axes.plot(lambda x: np.cos(x), color=GRAY, x_range=[-PI, 0])

        # Añadir al escenario
        self.play(Create(axes))
        self.play(Create(plot_sin))
        self.play(Create(plot_cos))
        self.wait()
class Plot3(Scene):
    def construct(self):
        self.camera.background_color = MAROON  # Fondo único para esta escena
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 10],
            axis_config={"include_numbers": True, "color": BLUE},
        )
        graph = axes.plot(lambda x: x**2, color=GREEN)
        self.play(Create(axes), Create(graph))
        self.wait()


class Plot4(Scene):
    def construct(self):
        self.camera.background_color = GOLD  # Fondo único para esta escena
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 10],
            axis_config={"include_numbers": True, "color": BLUE},
        )
        graph = axes.plot(lambda x: x**2, color=GREEN)
        self.play(Create(axes), Create(graph))
        self.wait()


class Plot5(Scene):
    def construct(self):
        self.camera.background_color = PURPLE  # Fondo único para esta escena
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"include_numbers": True, "color": BLUE},
        )
        graph = axes.plot(lambda x: x**2, color=GREEN)
        self.play(Create(axes), Create(graph))
        self.wait()


class Plot6(Scene):
    def construct(self):
        self.camera.background_color = RED  # Fondo único para esta escena
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"include_numbers": True, "color": BLUE},
        )
        graph = axes.plot(lambda x: x**2, color=GREEN)
        self.play(Create(axes), Create(graph))
        self.wait()


class Plot7(Scene):
    def construct(self):
        self.camera.background_color = GREEN  # Fondo único para esta escena
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"include_numbers": True, "color": BLUE},
        )
        graph = axes.plot(lambda x: x**2, color=GREEN)
        self.play(Create(axes), Create(graph))
        self.wait()


class PlotSinCos(Scene):
    def construct(self):
        self.camera.background_color = BLUE  # Fondo único para esta escena
        axes = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_numbers": True},
        )
        sin_graph = axes.plot(lambda x: np.sin(x), color=GREEN, x_range=[-3 * PI / 2, 3 * PI / 2])
        cos_graph = axes.plot(lambda x: np.cos(x), color=GRAY, x_range=[-PI, 0])

        self.play(Create(axes))
        self.play(Create(sin_graph))
        self.play(Create(cos_graph))
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
        description = Text("Plots 2D", font_size=24)
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