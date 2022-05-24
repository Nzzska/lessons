from manim import *
import numpy as np
import numpy.linalg as linalg

class PendulumScene(Scene):
    def update_pendulum(
        self,
        pendulum_obj,
        dt
    ):
        self.s += self.v*dt
        self.v += self.a*dt
        self.calc_angle()
        self.calculate_acceleration()
        pendulum_obj.move_to(self.s)

    def calculate_centripital_acceleration(self):
        a_c = linalg.norm(self.v)**2/self.thread_length + self.g * np.cos(self.angle)
        a_cx = a_c * np.sin(self.angle)
        a_cy = -1 * a_c * np.cos(self.angle) + self.g
        return np.array([a_cx, a_cy, 0.])

    def calculate_acceleration(self):
        a_c = self.calculate_centripital_acceleration()
        a_g = -1 * np.array([0., self.g, 0.])
        self.a = a_c + a_g

    def unit_vector(self, vector):
        return vector/linalg.norm(vector)

    def direction_towards(self, from_pos, to_pos):
        vec = to_pos - from_pos
        vec = self.unit_vector(vec)
        return vec

    def calc_angle(self):
        angl = np.arctan(
            (self.s[0]-self.pin_pos[0])/(self.s[1]-self.pin_pos[1])
        )
        print(self.s[0])
        self.angle = angl

    def construct(self):
        #given (init)
        self.m = 1
        self.g = 3
        self.v = np.array([0., 0., 0.])
        self.s = np.array([-3., 0., 0])
        self.a = np.array([0., 0., 0.])
        self.pin_pos = np.array([0., 4., 0.])

        #derived constants
        self.thread_length = linalg.norm(self.pin_pos - self.s)
        self.rest_position = self.pin_pos - np.array([0., self.thread_length, 0.])

        #derived variables
        self.calc_angle()


        ball = Circle(
            color=BLUE, 
            fill_opacity=1,
            radius=0.5
        ).shift(self.s)
        pin = Dot(color=RED).move_to(self.pin_pos)
        thread = Line(
            stroke_width=2, 
            color=WHITE, 
            start= ball.get_center(), 
            end=pin.get_center()
        ).add_updater(
            lambda m : m.put_start_and_end_on(
                ball.get_center(),
                pin.get_center()
            )
        )
        ball.add_updater(
            lambda m, dt: self.update_pendulum(m, dt) 
        )

        self.add(ball, pin, thread)
        self.play(ball.animate())
        self.wait(5)
