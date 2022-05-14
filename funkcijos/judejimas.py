from manim import *

def move_mobject(mobject, dt):
    mobject.shift(mobject.v)
    mobject.v += mobject.a

def kinetic_energy(mobject):
    mobject.KE = (mobject.m * mobject.v ** 2) / 2

def inelastic_collision(mobject, dt, target_mobject):
    total_p = mobject.p + target_mobject.p
    total_m = mobject.m + target_mobject.m

    mobject.v = total_p/total_m
    target_mobject.v = mobject.v
    mobject.a = 0
    target_mobject.a = 0
