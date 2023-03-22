#Plotting the derivative of a function
from manim import *
from math import *
# from random import random



#Input some func in terms of x as the only variable
func = '2**x'



class Canvas(Scene):

    def construct(self):
        Text.set_default(font='JuliaMono MediumItalic')

        #Axes Parameters
        self.x_range = (-1, 8)
        self.x_center = (self.x_range[0] + self.x_range[1])/2
        self.y_range = (-1, 50, 5)

        #Axes
        self.axes = Axes(
            self.x_range,
            self.y_range,
            axis_config={"include_numbers":True}            
            )
        self.add(self.axes)
        self.plot_graph_and_derivative(func)
        
        

    def plot_graph_and_derivative(self, func):
        #Creating the function f(x)
        def f(x):
            return eval(func)

        #Creating the graph for function and its label
        graph = self.axes.plot(f, color=random_color())
        graph_label = Text(str(func), font_size=DEFAULT_FONT_SIZE/2)
        graph_label.next_to(self.axes.coords_to_point(self.x_center,f(self.x_center), 0), DOWN+LEFT)
        self.play(Create(graph), run_time=3)
        self.play(Write(graph_label))
        self.wait()
        derivative = DashedVMobject(self.axes.plot_derivative_graph(graph, color=graph.get_color()), 30)
        derivative.set_opacity(0.8)
        self.play(Create(derivative), run_time=2.5)
        self.wait()
        graph.add_updater()

        
        


