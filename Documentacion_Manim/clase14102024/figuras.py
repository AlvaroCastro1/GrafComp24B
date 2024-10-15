from manim import *
import numpy as np

class Shapes(Scene):
    def construct(self):
        # Crear un círculo
        circulo = Circle()
        # Animación de creación (usando Create en lugar de ShowCreation)
        self.play(Create(circulo))
        # Animación de desaparición
        self.play(FadeOut(circulo))

        # Crear un rectángulo con color azul
        rect = Rectangle(color="blue", height=3, width=1)
        self.play(Create(rect))
        self.play(FadeOut(rect))

        # # Crear cuadrados y moverlos a posiciones específicas
        # cuadrado = Square()
        # cuadrado.move_to(np.array([-4, 2, 0]))  # Posicionar el cuadrado
        # cuadrado2 = Square()
        # cuadrado2.to_edge(UP)  # Mover el segundo cuadrado al borde superior
        # self.play(Create(cuadrado), Create(cuadrado2))
        # self.play(FadeOut(cuadrado), FadeOut(cuadrado2))

        # # Crear una línea entre dos puntos
        # linea = Line(np.array([2, 0, 0]), np.array([-2, 1, 0]))
        # self.play(Create(linea))
        # self.play(FadeOut(linea))


class AllShapes(Scene):
    def construct(self):
        self.anim(Arc(radius=0.5))
        self.anim(ArcBetweenPoints(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim(CurvedArrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim(CurvedDoubleArrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim(Circle())
        self.anim(Dot())
        self.anim(SmallDot())
        self.anim(Ellipse())
        self.anim(AnnularSector())
        self.anim(Sector())
        self.anim(Annulus())
        self.anim(Line(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim(DashedLine(np.array([2, 0, 0]), np.array([-2, 0, 0])))

        # Tangent line requires a mobject
        c = Circle()
        self.play(Create(c))
        self.anim(TangentLine(c, 0.2))
        self.play(FadeOut(c))

        self.anim(Elbow())
        self.anim(Arrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim(Vector(np.array([1, 0, 0])))
        self.anim(DoubleArrow(np.array([2, 0, 0]), np.array([-2, 0, 0])))
        self.anim(Polygon(np.array([2, 0, 0]), np.array([-2, 0, 0]), np.array([1, 1, 0]), np.array([-2, -3, 0])))
        self.anim(RegularPolygon(n=5))
        self.anim(Triangle())
        self.anim(ArrowTip())
        self.anim(Rectangle())
        self.anim(Square())
        self.anim(RoundedRectangle())

    def anim(self, mob):
        self.play(Create(mob))  # Usar Create en lugar de ShowCreation
        self.play(FadeOut(mob))
