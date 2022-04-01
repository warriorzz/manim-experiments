from manim import *


# noinspection PyTypeChecker
class VectorScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        dot0 = Dot3D(point=axes.coords_to_point(0, 0, 0), color=BLUE, fill_opacity=1)
        dotX1 = Dot3D(point=axes.coords_to_point(3, 0, 0), color=GREEN, fill_opacity=1)
        dotX2 = Dot3D(point=axes.coords_to_point(3, 2, 0), color=GREEN, fill_opacity=1)
        dotX3 = Dot3D(point=axes.coords_to_point(3, 2, 3), color=GREEN, fill_opacity=1)
        dotLine = Dot3D(point=axes.coords_to_point(0, 0, 0), color=BLACK, fill_opacity=1, radius=0.0001)

        lineX1 = Line3D(start=dot0.get_center(), end=dot0.get_center(), color=RED)

        xV = ValueTracker(0)
        yV = ValueTracker(0)
        zV = ValueTracker(0)

        graph = axes.plot(lambda z: z * 2 / 3, x_range=[0, 3], color=BLACK)
        area = axes.get_area(
            graph=graph, x_range=[0, 3], stroke_color=BLACK
        )

        x_tex = MathTex(r"x").move_to(
            axes.coords_to_point(1.5, -1 * MED_LARGE_BUFF, 0)
        )
        y_tex = MathTex(r"y").move_to(
            axes.coords_to_point(3 + MED_LARGE_BUFF, 1, 0)
        )
        formulaXY = MathTex(r"\sqrt{x^2 * y^2}").to_corner(UR)

        area3D = axes.get_area(
            graph=ParametricFunction(
                    lambda u: np.array([
                        u + axes.coords_to_point(0, 0, 0)[0],
                        u * 2 / 3 + axes.coords_to_point(0, 0, 0)[1],
                        u + axes.coords_to_point(0, 0, 0)[2]
                    ]), t_range=[3, 2, 3]
                ), x_range=[0, 3], stroke_color=BLACK
        )
        formulaXYZ = MathTex(r"\sqrt{\sqrt{x^2 * y^2} * z^2}").next_to(axes.coords_to_point(1, 0, 5)).rotate(angle=90 * DEGREES, axis=OUT)

        self.add(dot0, dotX1, dotX2, lineX1, axes, dotLine)

        self.wait(2)

        lineX1.add_updater(
            lambda z: z.become(
                Line3D(start=dot0.get_center(), end=dotLine.get_center(), color=RED)
            )
        )

        x1_updater = dotLine.add_updater(
            lambda z: z.set_x(xV.get_value())
        )
        self.play(
            xV.animate.set_value(dotX1.get_center()[0])
        )
        self.wait()
        lineX1.remove_updater(x1_updater)

        x2_updater = dotLine.add_updater(
            lambda z: z.set_y(yV.get_value())
        )
        self.play(
            yV.animate.set_value(dotX2.get_center()[1])
        )
        self.wait()
        lineX1.remove_updater(x2_updater)

        self.wait(3)
        self.play(Create(area))
        self.wait(3)
        # self.add(angle_x1x2)
        self.play(Write(x_tex))
        self.play(Write(y_tex))
        self.wait()
        self.wait(1)
        self.play(Write(formulaXY))
        self.wait(4)
        self.play(Unwrite(formulaXY))
        self.wait()

        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.wait()
        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta"
        )  # Rotates at a rate of radians per second
        self.wait(1)
        x3_updater = dotLine.add_updater(
            lambda z: z.set_z(zV.get_value())
        )
        self.play(
            zV.animate.set_value(dotX3.get_center()[2])
        )
        self.wait()
        lineX1.remove_updater(x3_updater)
        self.add(dotX3)
        self.wait(1)
        self.play(Create(area3D))
        self.wait(1)
        self.play(Write(formulaXYZ))
        self.wait(5)
