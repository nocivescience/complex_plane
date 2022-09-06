from manim import *
class ComplexScene(Scene):
    def construct(self):
        axes=ComplexPlane()
        dot=Dot().move_to(axes.number_to_point(complex(1,2)))
        dot_copy=dot.copy()
        dot_copy.move_to(axes.number_to_point(complex(-2,1)))
        self.play(Create(axes),Create(dot),Create(dot_copy))
        self.wait()