from manim import *
from random import random


#To verify the bertrand's paradox

sample_size = 1000
max_animation_time = 1.25
complete_anim_for_chords = 12



class Canvas(Scene):
    def construct(self):
        circle_radius = 2
        self.circle = Circle(circle_radius)
        triangle = Triangle(color=DARK_BLUE, stroke_width=0.75, fill_opacity=0.1).scale(2)
        triangle.align_to(self.circle, UP)
        self.bigger_count = 0
        self.total = 0

        #Adding text
        text1 = Text(f'{self.bigger_count}')
        text2 = Text(f'{self.total}')
        text3 = Text(f'{0}')
        text2.next_to(text1, DOWN, 0.1)
        text3.next_to(text2.get_corner(RIGHT+UP)+(0, -0.05, 0))
        self.text_group = VGroup(text1, text2, text3)
        self.text_group.next_to(self.circle, RIGHT, 2)

        self.play(Create(self.circle), Write(self.text_group), Create(triangle), run_time=2)
        self.wait()
    
        
        for index in range(sample_size):
            if index < complete_anim_for_chords:
                animation_duration = max_animation_time * (1-(rate_functions.slow_into(1)*index/complete_anim_for_chords))
            else:
                animation_duration = 0
            self.draw_chord2(self.generate_chord2(self.circle), animation_duration)
        self.wait()
        
        

#META 1

    def generate_chord1(self, circle):
        """Generates a random chord, by taking two random points on the circle and joining them with a line""" 
        dot1 = Dot(circle.point_at_angle(2*PI*random()), color=GREEN, radius=DEFAULT_DOT_RADIUS/2)
        dot2 = Dot(circle.point_at_angle(2*PI*random()), color=GREEN, radius=DEFAULT_DOT_RADIUS/2)
        chord = Line(dot1.get_center(), dot2.get_center(), color=BLUE, stroke_width=1)
        return VGroup(dot1, dot2, chord)

    def draw_chord1(self, chord_group, animation_duration):
        """Drawing a chord onto the canvas"""
        if animation_duration == 0:
            self.add(chord_group)
            self.wait(0.1)
        else:
            time_for_points = animation_duration/3
            time_for_line = 2*animation_duration/3
            #Creating the points
            self.play(Create(chord_group[0]), Create(chord_group[1]), run_time=time_for_points)
            #Creating the line
            self.play(Create(chord_group[2]), run_time=time_for_line)


#META2

    def generate_chord2(self, circle):
        seed1 = random()
        seed2 = random()
        if abs(seed1-seed2)>(2/3) or abs(seed1-seed2)<(1/3):
            color = WHITE
            bigger = False
        else:
            color = BLUE
            bigger = True
        chord = Line(circle.point_at_angle(2*PI*seed1), circle.point_at_angle(2*PI*seed2), stroke_width=0.8, color=color)

        return [chord, bigger] 
    
    def draw_chord2(self, chord, animation_duration):
        self.update_text(chord[1])
        if animation_duration == 0:
            self.add(chord[0])
            self.add(self.text_group)      
            self.wait(0.075)
        else:
            self.play(Create(chord[0]), Write(self.text_group), run_time=animation_duration)

    def update_text(self, boolean):
        self.total += 1
        if boolean:
            self.bigger_count += 1

        text1 = Text(f'{self.bigger_count}')
        text2 = Text(f'{self.total}')
        text3 = Text(f'{str(self.bigger_count/self.total)[:4]}')
        text2.next_to(text1, DOWN, 0.1)
        text3.next_to(text2.get_corner(RIGHT+UP)+(0, -0.05, 0))
        self.remove(self.text_group)
        self.text_group = VGroup(text1, text2, text3)
        self.text_group.next_to(self.circle, RIGHT, 2)


