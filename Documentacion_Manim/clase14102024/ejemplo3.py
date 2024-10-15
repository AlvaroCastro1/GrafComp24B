from manim import *

class UpdatersExample(Scene):
    def construct(self):
        # Crear un cuadrado y un número decimal
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
