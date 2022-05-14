from manim import *


class Demo(Scene):
    def construct(self):

        x = np.linspace(0, 20, 5)
        y = [1,-1,1,-1,1]

        ball = Circle(color=BLUE, fill_opacity=1)
        self.add(ball)
        t=0
        for i in range(len(x)):
            self.play(ball.animate(run_time= float(x[i]+0.01-t)).shift(LEFT*y[i]))
            t=x[i]
        self.wait()
