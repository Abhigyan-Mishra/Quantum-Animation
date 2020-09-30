from manimlib.imports import *

class SphereFromIPSpace(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(70*DEGREES, 300*DEGREES)
        self.camera.frame_center.shift(UR)

        plane = NumberPlane(
            background_line_style = {"stroke_color": GREY},
            x_axis_config = {"x_min":-1, "x_max": 5, "stroke_color":MAROON},
            y_axis_config = {"x_min":-1, "x_max": 8, "stroke_color":GREEN}
        )

        dx, dy = 0.2, 0.2
        sphere_rects = VGroup()
        
        for x in np.arange(0, PI, dx):
            for y in np.arange(0, 2*PI, dy):
                rect = Rectangle(width=dx, height=dy, fill_opacity=0.6)
                rect.shift((x+dx/2)*RIGHT + (y+dy/2)*UP)
                sphere_rects.add(rect)
                
        sphere_rects.set_color_by_gradient(BLUE, GREEN, MAROON)
        self.add(plane, sphere_rects)
        self.wait()

        def param_func(point):
            u, v = point[:-1]
            return np.array([
                np.cos(v) * np.sin(u),
                np.sin(v) * np.sin(u),
                np.cos(u)
            ])

        self.play(
            LaggedStart(
                *[ApplyMethod(mob.apply_function, param_func, lag_ratio=0.5)
                for mob in sphere_rects]
            ),
            run_time = 8
        )
        self.wait()

class ConeScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(70*DEGREES, 300*DEGREES)
        self.camera.frame_center.shift(UR)

        plane = ThreeDAxes(
            # background_line_style = {"stroke_color": GREY},
            x_axis_config = {"x_min":-1, "x_max": 5, "stroke_color":MAROON},
            y_axis_config = {"x_min":-1, "x_max": 8, "stroke_color":GREEN},
            z_axis_config = {"x_min":-1, "x_max": 5, "stroke_color":BLUE},
        )

        dr, dphi = 0.2, 0.2
        cone_rects = VGroup()
        
        for r in np.arange(0, 2, dr):
            for phi in np.arange(0, 2*PI, dphi):
                rect = Rectangle(width=dr, height=dphi, fill_opacity=0.6)
                rect.shift((r+dr/2)*RIGHT + (phi+dphi/2)*UP)
                cone_rects.add(rect)
        
        cone_rects.set_color_by_gradient(BLUE, GREEN, MAROON)
        self.add(plane, cone_rects)
        self.wait()

        theta = PI/6
        def param_func(point):
            r, phi, _ = point
            return np.array([
                r * np.sin(theta) * np.cos(phi),
                r * np.sin(theta) * np.sin(phi),
                r * np.cos(theta)
            ])

        self.play(
            LaggedStart(
                *[ApplyMethod(mob.apply_function, param_func, lag_ratio=0.5)
                for mob in cone_rects]
            ),
            run_time = 8
        )
        self.wait()

class ConeScene2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(70*DEGREES, 300*DEGREES)
        # self.set_camera_orientation(0*DEGREES, 0*DEGREES)
        self.camera.frame_center.shift(UR)
        
        plane = ThreeDAxes(
            background_line_style = {"stroke_color": GREY},
            x_axis_config = {"x_min":-1, "x_max": 5, "stroke_color":MAROON},
            y_axis_config = {"x_min":-1, "x_max": 8, "stroke_color":GREEN},
            z_axis_config = {"x_min":-1, "x_max": 5, "stroke_color":BLUE},
        )

        cone = Cone(direction=Y_AXIS)
        # cone = Cone()

        a2 = Arrow(-Y_AXIS+X_AXIS, 2*Y_AXIS+X_AXIS)
        a3 = Arrow3d(-Y_AXIS, 2*Y_AXIS)
        a32 = Arrow3d(-X_AXIS, X_AXIS)
        a33 = Arrow3d(-Z_AXIS, Z_AXIS)
        self.add(plane, a2, a3, a32, a33)
        self.wait()

