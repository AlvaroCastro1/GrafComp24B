from manim import *

class CameraPosition1(ThreeDScene):
    def construct(self):
        self.camera.background_color = DARK_GRAY  # Fondo único
        circle = Circle()
        self.play(Create(circle))
        self.wait()


class CameraPosition2(ThreeDScene):
    def construct(self):
        self.camera.background_color = GRAY  # Fondo único
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition3(ThreeDScene):
    def construct(self):
        self.camera.background_color = TEAL  # Fondo único
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition4(ThreeDScene):
    def construct(self):
        self.camera.background_color = ORANGE  # Fondo único
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition5(ThreeDScene):
    def construct(self):
        self.camera.background_color = MAROON  # Fondo único
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


class MoveCamera1(ThreeDScene):
    def construct(self):
        self.camera.background_color = PURPLE  # Fondo único
        axes = ThreeDAxes()
        circle = Circle()
        self.play(Create(circle), Create(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()


class MoveCamera2(ThreeDScene):
    def construct(self):
        self.camera.background_color = GOLD  # Fondo único
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)
        self.wait()


class ParametricCurve1(ThreeDScene):
    def construct(self):
        self.camera.background_color = GREEN  # Fondo único
        axes = ThreeDAxes()
        curve1 = ParametricFunction(
            lambda u: np.array([1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]),
            color=RED,
            t_range=[-TAU, TAU],
        )
        curve2 = ParametricFunction(
            lambda u: np.array([1.2 * np.cos(u), 1.2 * np.sin(u), u]),
            color=RED,
            t_range=[-TAU, TAU],
        )
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()


class ParametricCurve2(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLUE  # Fondo único
        axes = ThreeDAxes()
        curve1 = ParametricFunction(
            lambda u: np.array([1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]),
            color=RED,
            t_range=[-TAU, TAU],
        )
        curve2 = ParametricFunction(
            lambda u: np.array([1.2 * np.cos(u), 1.2 * np.sin(u), u]),
            color=RED,
            t_range=[-TAU, TAU],
        )
        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()


class SurfacesAnimation(ThreeDScene):
    def construct(self):
        self.camera.background_color = RED  # Fondo único
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u),
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            checkerboard_colors=[RED_D, RED_E],
        )
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.add(axes)
        self.play(Create(sphere))
        self.wait()


class Text3D1(ThreeDScene):
    def construct(self):
        self.camera.background_color = GRAY  # Fondo único
        axes = ThreeDAxes()
        text3d = Text("This is a 3D text").scale(2)

        # Añadimos una animación para que genere un video
        self.play(Create(axes))
        self.play(Write(text3d))
        self.wait(2)



class Text3D2(ThreeDScene):
    def construct(self):
        self.camera.background_color = PINK  # Fondo único
        axes = ThreeDAxes()
        text3d = Text("This is a 3D text").scale(2).rotate(PI / 2, axis=RIGHT)

        # Configuración inicial de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Animaciones
        self.play(Create(axes))  # Crear los ejes
        self.play(Write(text3d))  # Escribir el texto
        self.wait(1)

        # Cambiar la cámara para apreciar mejor el texto
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=3)
        self.wait(2)



class Text3D3(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLUE_E  # Fondo único
        axes = ThreeDAxes()
        text3d = Text("This is a 3D text")

        # Añadir el texto en un plano fijo
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)  # Mover el texto a la esquina superior izquierda

        # Configuración inicial de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Añadir animaciones
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.1)  # Animar rotación de la cámara
        self.play(Write(text3d))  # Escribir el texto
        self.wait(2)

        # Movimiento de la cámara para apreciar mejor el entorno
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=3)
        self.wait(2)

        # Mostrar un objeto 3D (esfera) junto al texto
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            checkerboard_colors=[RED_D, RED_E],
        ).scale(2)

        self.play(Create(sphere))
        self.wait(2)

class Alvaro(Scene):
    def construct(self):
        # Título principal
        title = Text("ALVARO JESUS CASTRO PIZAÑA", font_size=36, weight=BOLD)
        title.to_edge(UP)  # Mover el título a la parte superior

        # Subtítulo
        subtitle = Text("2125698", font_size=28, slant=ITALIC)
        subtitle.next_to(title, DOWN)  # Colocar debajo del título

        # Descripción del contenido
        description = Text("Plots 3D", font_size=24)
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