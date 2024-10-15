from manim import *

class MoveSquaresToCorners(Scene):
    def construct(self):
        # Crear 5 cuadrados
        cuadrado1 = Square(color=BLUE)
        cuadrado2 = Square(color=RED)
        cuadrado3 = Square(color=GREEN)
        cuadrado4 = Square(color=YELLOW)
        cuadrado5 = Square(color=PURPLE)

        # Mover los cuadrados a las esquinas y uno al centro
        cuadrado1.to_corner(UP + LEFT)      # Esquina superior izquierda
        cuadrado2.to_corner(UP + RIGHT)     # Esquina superior derecha
        cuadrado3.to_corner(DOWN + LEFT)    # Esquina inferior izquierda
        cuadrado4.to_corner(DOWN + RIGHT)   # Esquina inferior derecha
        cuadrado5.to_corner(ORIGIN)         # Centro

        # Añadir los cuadrados a la escena
        self.play(Create(cuadrado1), Create(cuadrado2), Create(cuadrado3), Create(cuadrado4), Create(cuadrado5))

        # Esperar un momento antes de cerrar la escena
        self.wait()
