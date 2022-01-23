from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .forms import ScoreForm

ExamModel = apps.get_model("database", "Exam")
CourseListingModel = apps.get_model("database", "CourseListing")
# BAD :(
from database.models import *

def get_score(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScoreForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            if (form.cleaned_data['your_score'] > 100):
                form.cleaned_data['your_score'] = 100
            
            # Getting parameters from url for Course Title
            course_title = form.cleaned_data['your_course']
            course_dept = course_title.split(" ")[0].lower()
            course_num = course_title.split(" ")[1]
            print(course_dept)
            print(course_num)

            courses = get_all_courses()
            create_course(department=course_dept, number=course_num)
            found_course = None
            for course in courses:
                if (course.department == course_dept and course.course_number == str(course_num)):
                    print("found in loop")
                    found_course = course
            if (found_course != None):
                print("found course")
                create_exam(found_course, float(form.cleaned_data['your_score']))
                print("Current Exams")
                exams = get_exams_for_course(found_course)
                for exam in exams:
                    print(exam.score)
            
            # get_course("ECE", 20875)
            #create_course(department="ece", number=20875)
            # print(courses)
            print("Got Post Request")
            print(form.cleaned_data['your_score'])
            print(type(form.cleaned_data['your_score']))
            print(form.cleaned_data['your_grade'])
            return HttpResponseRedirect('/pphomepage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScoreForm()

    return render(request, 'score.html', {'form': form})
