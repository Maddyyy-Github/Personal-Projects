import random
from manim import *
from matplotlib.pyplot import arrow, text

#To simulate bell's inequalities
#What do I want:
#2 entangled particles entering 2 detectors that detect spin


orientation_of_particle_spin = 0.25 #returns a number between 0 and 1
print(orientation_of_particle_spin)



class Particles(Scene):

    def construct(self):
        self.radius = 1
        self.rotation_angle = orientation_of_particle_spin * 2 * PI
        particle1 = Circle(self.radius, BLUE_B)
        particle2 = Circle(self.radius, BLUE_C)
        spin_direction_arrow1 = Arrow(
            start=ORIGIN, end=UP*self.radius, 
            color=interpolate_color(GREEN, RED, 2*abs(orientation_of_particle_spin - 0.5)), 
            buff=0
            )
        spin_direction_arrow1.rotate(self.rotation_angle, about_point=ORIGIN)
        spin_direction_arrow2 = spin_direction_arrow1.copy()
        spin_direction_arrow2.set_color(interpolate_color(RED, GREEN, 2*abs(orientation_of_particle_spin - 0.5)))
        spin_direction_arrow2.rotate(PI, about_point=ORIGIN)
        particle_set1 = Group(particle1, spin_direction_arrow1)
        particle_set2 = Group(particle2, spin_direction_arrow2)
        particle_set1.to_corner(LEFT + UP)
        particle_set2.next_to(particle_set1, RIGHT)
        text = Text(str(orientation_of_particle_spin))

        self.add(particle_set1, particle_set2, text)


# particles = Particles()


