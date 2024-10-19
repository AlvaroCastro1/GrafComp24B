from manim import *

class disenio(Scene):
    def construct(self):
        # Crear el cuerpo principal como una elipse
        cuerpo = Ellipse(width=5, height=2, color=BLUE, fill_opacity=1)
        cuerpo.shift(UP*1)

        # Crear los ojos como pequeños triángulos
        ojo1 = Polygon([-0.5, 0.2, 0], [-0.2, 0.2, 0], [-0.35, 0.5, 0], color=WHITE, fill_opacity=1)
        ojo2 = Polygon([0.5, 0.2, 0], [0.2, 0.2, 0], [0.35, 0.5, 0], color=WHITE, fill_opacity=1)
        
        ojo1.shift(UP*0.4)
        ojo2.shift(UP*0.4)

        # Crear los brazos como rectángulos rotados
        brazo1 = Rectangle(width=2, height=0.5, color=BLUE, fill_opacity=1)
        brazo2 = Rectangle(width=2, height=0.5, color=BLUE, fill_opacity=1)
        
        brazo1.rotate(PI/8)
        brazo2.rotate(-PI/8)

        brazo1.shift(LEFT*3 + UP*0.5)
        brazo2.shift(RIGHT*3 + UP*0.5)

        # Crear las piernas como cuadrados
        pierna1 = Square(side_length=0.7, color=BLUE, fill_opacity=1)
        pierna2 = Square(side_length=0.7, color=BLUE, fill_opacity=1)
        
        pierna1.shift(LEFT*0.75 + DOWN*1.5)
        pierna2.shift(RIGHT*0.75 + DOWN*1.5)

        # Crear los pies como pequeños triángulos
        pie1 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=BLUE, fill_opacity=1)
        pie2 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=BLUE, fill_opacity=1)

        pie1.shift(LEFT*0.75 + DOWN*2.1)
        pie2.shift(RIGHT*0.75 + DOWN*2.1)

        # Añadir todos los elementos a la escena
        self.add(cuerpo, ojo1, ojo2, brazo1, brazo2, pierna1, pierna2, pie1, pie2)

        self.wait(3)
