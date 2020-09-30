from manimlib.imports import *

class ConeScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(70*DEGREES, 300*DEGREES)
        self.camera.frame_center.shift(UR)


        a = Arrow3d(-Y_AXIS, 2*Y_AXIS)
        self.add(a)

        cone = Cone(direction=Y_AXIS)
        self.add(cone)

        self.wait()
