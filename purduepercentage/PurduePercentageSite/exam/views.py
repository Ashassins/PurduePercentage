from django.shortcuts import render

from bokeh.embed import components
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show

import numpy as np
import math

from database.models import *

def hex_two_rgb(hex) -> tuple :
    hex = hex.lstrip('#')
    rgb = tuple(int(hex[i:i + len(hex) // 3]) for i in range(0, len(hex), len(hex) // 3))
    return rgb

def rgb_two_hex(rgb) -> str :
    string = "#"
    return string.append(str(hex(rgb[i])) for i in range(0, 3)) 

def interpolate(rgb1 : tuple, rgb2 : tuple) -> tuple:
    params = List(tuple(rgb2[i] - rgb1[i], rgb1[i]) for i in range(0, len(rgb1))) 
    return params

def grad(codes : List, n : int) -> List :
    rgb_vals = [hex_two_rgb(codes[i] for i in range(0, len(codes)))]
    
    # linerly interpolate between each points
    interpol = []
    interpol.append(interpolate(rgb_vals[i+1], rgb_vals[i]) for i in range(0, len(rgb_vals) - 1))

    for j in np.linspace(0, 8, n) :
        bucket = interpol[round(j)]
        rgb = tuple(int(bucket[0][0] * j + bucket[0][1]))

    return hex_grad

def histo(p, hist, edges):
    #p = figure(title=title, tools='', background_fill_color="#fafafa")
    # creates a quadrilateral for each of the buckets and sets the height relative to the frequency
    # can add color based on the data
    colors = ['#F72585', '#B5179E', '#7209B7','#560BAD', '#480CA8', '#3A0CA3', '#3F37C9', '#4361EE', '#4895EF', '#4CC9F0']
    #r_g_b_a = {"r" : [], "g" : [], "b" : [], "a" : []}

    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color=colors, line_color="#B5179E", alpha=0.5) 

    # plot formatting
    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'x'
    p.yaxis.axis_label = 'Pr(x)'
    p.grid.grid_line_color="white"

    return p

def scatter(p, hori, vert) :
    # add coloring based on the data
    sz = 0.1
    p.scatter(x = hori, y = vert, size = sz)
    
    # plot formatting
    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'x'
    p.yaxis.axis_label = 'Pr(x)'
    p.grid.grid_line_color="white"

    return p

def pie(p) :

    # plot formatting

    return p
    
def boxandwhisker(p) :
    
    # plot formatting
    
    return p

# Create your views here.
def exam(request):  
# SQL Data Calls (Dummy Data, remove random number generation and the change measured to the data from the SQL database)
    dat = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5] # JACKSONS COOL PULL FUNCTION
    courses = get_all_courses()
    create_course(department="ece", number=20875)
    found_course = None
    for course in courses:
        if (course.department == "ece" and course.course_number == "20875"):
            # print("found in loop")
            found_course = course
    if (found_course != None):
        print("found course")
        print("Current Exams")
        exams = get_exams_for_course(found_course)
        dat.clear()
        for exam in exams:
            dat.append(exam.score)
    hist, edges = np.histogram(dat, density=True, bins=round(math.sqrt(len(dat))))
    exam_avg = round(sum(dat) / len(dat))

# Plot
    plot = figure(title = "test")
    plot = scatter(plot, dat, dat) #histo(plot, hist, edges)

# Write script and div
    script, div = components(plot)

    return render(request, 'exam.html', 
        {'script': script, 'div': div, 'exam_avg': exam_avg} )