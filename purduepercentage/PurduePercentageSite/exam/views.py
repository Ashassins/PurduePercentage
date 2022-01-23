from django.shortcuts import render

from bokeh.embed import components
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show

import numpy as np
import math

from database.models import *

def histo(p, hist, edges):
    #p = figure(title=title, tools='', background_fill_color="#fafafa")
    # creates a quadrilateral for each of the buckets and sets the height relative to the frequency
    # can add color based on the data
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5) 

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
    p.scatter(x = hori, y = vert, size = sz, marker = "asterix")
    
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
    plot = histo(plot, hist, edges)

# Write script and div
    script, div = components(plot)

    return render(request, 'exam.html', 
        {'script': script, 'div': div, 'exam_avg': exam_avg} )