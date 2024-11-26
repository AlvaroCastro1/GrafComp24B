from manim import *
from laboratorio_de_gelipe import FondoLaboratorio

class EscenaConFondo(Scene):
    def construct(self):
        # Crear el fondo del laboratorio
        fondo = FondoLaboratorio.crear_fondo()
        
        # Añadir el fondo a la escena
        self.add(fondo)

        # Añadir más objetos o animaciones
        texto = Text("Laboratorio en construcción").to_edge(UP)
        self.add(texto)

        self.wait(5)
