# from prime_factorize import check_prime
# from time import time
from manim import *
from math import ceil, sqrt


#Z1 = a + bi
#Z2 = c - di
#Z1^2 + Z2^2 = R^2 (Equation of a complex circle)
#for R being a real number, the products of real and imaginary part of Z1 and Z2 must be the same, leaving:
# a^2 + b^2 + c^2 - (a^2 * b^2)/(c^2) = R^2
#THIS PROGRAM FINDS INTEGER SOLUTIONS FOR A,B,C FOR R=1 IN THE ABOVE EQUATION


#Few observations:
#a != c, b != c, either one of a and b are non prime. c can not be 0
#for our code, a will never be a prime


# initial_time = time()
# search_size = 100
# a=1
# b=1
# c=1
# r_squared = 1
# r_squared_range = 1000
# r_squared_valid = []
# for number in range(-r_squared_range, r_squared_range):
#     r_squared = number
#     # print(f'\n\n--\t{r_squared}\t--\n\n')
#     a=1
#     b=1
#     c=1
#     for num1 in range(search_size):
#         a += 1
#         if check_prime(a) is False:
#             b = 1
#             for num2 in range(search_size):
#                 b += 1
#                 c = 1
#                 for num3 in range(search_size):
#                     c += 1
#                     if (a*b)%c == 0 and c!=a and c!=b:
#                         if (a**2 + b**2 + c**2 - (((a**2)*(b**2))/(c**2))) == r_squared:
#                             if r_squared not in r_squared_valid:
#                                 r_squared_valid.append(r_squared)
                            # print(f'Z1 = {a} + {b}i,\tZ2 = {c} - {int(a*b/c)}i')

        # if a%100 == 0:
            # print(f"Searching in a = {a}...")
# for r_square in r_squared_valid:
#     print(r_square)

    
NumberPlane()


class ComplexCircle(Scene):
    def construct(self):
        #Setup

        #complex_plane
        x_range = (-7, 7)
        x_len = x_range[1] - x_range[0]
        y_range = (-7, 7)
        y_len = y_range[1] - y_range[0]
        complex_plane1 = ComplexPlane(x_range=x_range, y_range=y_range).add_coordinates()
        self.play(Create(complex_plane1), run_time=3)
        self.wait()
        self.play(complex_plane1.animate.scale(0.45))
        complex_plane2 = complex_plane1.copy()
        self.add(complex_plane2)
        self.play(complex_plane1.animate.to_edge(LEFT), complex_plane2.animate.to_edge(RIGHT))
        self.wait()
        #labelling
        text1 = Text('Input').next_to(complex_plane1, UP)
        text2 = Text('Output').next_to(complex_plane2, UP)
        self.play(Write(text1), Write(text2), run_time=1.5)
        #func
        f_text = MarkupText("Z<sup><sup><big>2</big></sup></sup><sub><sub><big>1</big></sub></sub> + Z<sup><sup><big>2</big></sup></sup><sub><sub><big>2</big></sub></sub> = 1").scale(0.8).to_edge(DOWN, buff=0) #Thats just Z1^2 + Z2^2 = 1, I just didn't like the look of simple sub and sup so altered it
        self.play(Write(f_text))
        self.wait()


        #Function PLot

        #Z1^2 + Z2^2 = 1 is only possible if the imaginary term in both Z1^2 and Z2^2 cancel
        #That is to assume Z1 = a + bi, Z2 = c - di, ab = cd
        #Solving furthur, a^2 + b^2 + c^2 - (a^2*b^2)/(c^2) is = Z1^2 + Z2^2 = 1
        # => letting c^2 as C: C^2 + C(a^2 + b^2 - 1) - (a^2 + b^2) = 0
        # => C = (1 - (a^2 + b^2) + sqrt( (1 - (a^2 + b^2))^2  + 4*(a^2 + b^2)))/2    {from quadratic formula}
        detail = 0.5
        dot_radius = 0.45 * 0.75 * detail / 2
        output_zoom = 10

        #Fixing Complex plane 2 range
        self.play(FadeOut(complex_plane2))
        complex_plane2 = ComplexPlane(x_range=(x_range[0]*output_zoom, x_range[1]*output_zoom, output_zoom), y_range=(y_range[0]*output_zoom, y_range[1]*output_zoom, output_zoom)).add_coordinates().scale(0.45/output_zoom).to_edge(RIGHT)
        self.play(FadeIn(complex_plane2))
        self.wait()

        color_gradient_list = color_gradient([RED, BLUE, GREEN], ceil((x_len+y_len)/detail)) 
        #Creating dots
        input_dots = VGroup()
        output_dots = VGroup()
        for a in range(int(x_len/detail)):
            for b in range(int(y_len/detail)):
                x = x_range[0]+a*detail
                y = y_range[0]+b*detail
                output = self.func(x, y)
                dot = Dot(complex_plane1.c2p(x, y), dot_radius, color=color_gradient_list[int(a+b)])
                input_dots.add(dot)
                dot = Dot(complex_plane2.c2p(output[0], output[1]), dot_radius/sqrt(output_zoom), color=color_gradient_list[int(a+b)])
                output_dots.add(dot)
        self.play(Create(input_dots), run_time=2)
        self.wait(1)
        self.play(Create(output_dots), run_time=2)
        self.wait()
            

    def func(self, a, b):
        c = sqrt(1 - (a**2 + b**2) + sqrt( (1 - (a**2 + b**2))**2  + 4*(a**2 + b**2)))/2
        try:
            d = a*b/c
        except:
            d = 0
        return (c, d)


        
        
        
        
        



