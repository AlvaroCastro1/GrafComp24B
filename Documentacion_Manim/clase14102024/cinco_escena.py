from manim import *

class principal(Scene):
    def construct(self):
#------------------------------------------------------------------------------------------------------------------------------------------------------#
        # crear cuadrado y pasar a fragmento de rueda
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()

        # Quitar el cuadrado para dar paso a la siguiente escena
        self.play(FadeOut(square))

#------------------------------------------------------------------------------------------------------------------------------------------------------#
        # Crear el texto y mostrarlo junto con una función
        example_text = Text("Alvaro Jesus Castro Pizaña")
        example_text.set_color_by_t2c({"text": YELLOW})  # Colorear la palabra "text" de amarillo

        # Crear una expresión matemática con los delimitadores correctos
        example_tex = Tex(
            "$\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}$"
        )
        
        # Agrupar ambos objetos y organizarlos
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config.frame_width - 2 * LARGE_BUFF)

        # Animaciones
        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()

        # Quitar el texto y la expresión para dar paso a la siguiente escena
        self.play(FadeOut(group))

#------------------------------------------------------------------------------------------------------------------------------------------------------#
        # Crear un cuadrado y número decimal
        square = Square()
        decimal = DecimalNumber()
        
        # Agregar actualizadores al decimal para que siga al cuadrado
        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))

        # Añadir el cuadrado y el decimal a la escena
        self.add(square, decimal)

        # Animar el cuadrado usando .animate
        self.play(
            square.animate.to_edge(DOWN),  # Usar animate en lugar de pasar el método directamente
            rate_func=there_and_back,
            run_time=5,
        )

        # Detener los actualizadores cuando termine la animación
        square.clear_updaters()
        decimal.clear_updaters()
        self.wait()

        # Quitar el cuadrado y el número decimal
        self.play(FadeOut(square), FadeOut(decimal))

#------------------------------------------------------------------------------------------------------------------------------------------------------#
        # crear circulo y un rectángulo

        # Crear un círculo
        circulo = Circle()
        self.play(Create(circulo))
        self.wait()
        
        # Quitar el círculo
        self.play(FadeOut(circulo))

        # Crear un rectángulo con color azul
        rect = Rectangle(color="blue", height=3, width=1)
        self.play(Create(rect))
        self.play(FadeOut(rect))

#------------------------------------------------------------------------------------------------------------------------------------------------------#
        # Crear 5 cuadrados de diferentes colores
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
        cuadrado5.move_to(ORIGIN)           # Centro

        # Añadir los cuadrados a la escena
        self.play(Create(cuadrado1), Create(cuadrado2), Create(cuadrado3), Create(cuadrado4), Create(cuadrado5))

        # Esperar un momento antes de cerrar la escena
        self.wait()

        # Quitar los cuadrados antes de terminar
        self.play(FadeOut(cuadrado1), FadeOut(cuadrado2), FadeOut(cuadrado3), FadeOut(cuadrado4), FadeOut(cuadrado5))
