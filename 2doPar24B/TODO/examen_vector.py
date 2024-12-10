from manim import *

# ahora es en 3d
class ejercicio3(ThreeDScene):
    def construct(self):
        # formula para ver si son ortogonales
        vector_u = MathTex(r"\vec{u} = \langle a, b, c \rangle")
        vector_v = MathTex(r"\vec{v} = \langle -b, a, 0 \rangle")
        vectors_text = VGroup(vector_u, vector_v).arrange(DOWN, buff=0.5).to_edge(UP)

        # producto punto
        producto_punto = MathTex(
            r"\vec{u} \cdot \vec{v} = u_1v_1 + u_2v_2 + u_3v_3"
        ).next_to(vectors_text, DOWN, buff=1)

        # sustituir valores
        sustitucion = MathTex(
            r"\vec{u} \cdot \vec{v} = (a)(-b) + (b)(a) + (c)(0)"
        ).next_to(producto_punto, DOWN, buff=1)
        
        # resultado
        resultado = MathTex(
            r"\vec{u} \cdot \vec{v} = -ab + ab + 0 = 0"
        ).next_to(sustitucion, DOWN, buff=1)

        # son ortogonales
        resultado_ortogonal = Text(
            "Los vectores son ortogonales",
            color=GREEN
        ).scale(0.7).next_to(resultado, DOWN, buff=1)


        # Animación de los pasos
        self.play(Write(vector_u))
        self.play(Write(vector_v))
        self.wait(1)
        self.play(Write(producto_punto))
        self.wait(1)
        self.play(Write(sustitucion))
        self.wait(1)
        self.play(Write(resultado))
        self.wait(1)
        self.play(Write(resultado_ortogonal))
        
        # limpiar pantalla
        self.play(
            FadeOut(vector_u),
            FadeOut(vector_v),
            FadeOut(producto_punto),
            FadeOut(sustitucion),
            FadeOut(resultado)
        )

        # grafica para vectores
        axes = ThreeDAxes()  # ejes 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # dejar la vista correcta

        # ejemplo de vectores
        u = [2, 3, 1] 
        v = [-3, 2, 0]

        # crear vectores
        vec_u = Arrow3D(start=[0, 0, 0], end=u, color=BLUE)
        vec_v = Arrow3D(start=[0, 0, 0], end=v, color=RED)

        etiqueta_u = Text("u", color=BLUE).move_to([2, 3, 1.5])
        etiqueta_v = Text("v", color=RED).move_to([-3, 2, 0.5])

        # Agregar ejes y vectores
        self.play(Create(axes))  # Crear los ejes
        self.play(Create(vec_u), Write(etiqueta_u))
        self.play(Create(vec_v), Write(etiqueta_v))
        self.wait(2)