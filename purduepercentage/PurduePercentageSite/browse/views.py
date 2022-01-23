from django.shortcuts import render
from database.models import *

def filter_dept(courses, dept):
    filtered_courses = []
    for course in courses:
        if (course.department == dept.lower()):
            filtered_courses.append(course)
    return filtered_courses

def filter_num(courses, num):
    filtered_courses = []
    for course in courses:
        if (course.course_number == str(num)):
            filtered_courses.append(course)
    return filtered_courses

# Create your views here.
def browse(request):
    dept_filter = None
    num_filter = None
    if(request.POST):
        print("Post")
        print(request.POST['selected_dept'])
        print(request.POST['selected_number'])
        dept_filter = request.POST['selected_dept']
        num_filter = request.POST['selected_number']


    field_names = ['Course Code', 'Exam Average']
    courses = get_all_courses()
    course_names = [c.department.upper() + " " + str(c.course_number) for c in courses]
    depts = list(set([c_n.split(" ")[0] for c_n in course_names]))
    if (dept_filter != None and dept_filter != "ALL"):
        courses = filter_dept(courses, dept_filter)
    if (num_filter != None and num_filter != ""):
        courses = filter_num(courses, num_filter)
    course_names = [c.department.upper() + " " + str(c.course_number) for c in courses]
    print(course_names)
    exams_set = [get_exams_for_course(c) for c in courses]
    # for exams in exams_set:
    exams_scores_only = [[e.score for e in exams] for exams in exams_set]
    exam_avgs_set = [round(sum(exams) / len(exams)) for exams in exams_scores_only]
    print(exam_avgs_set)
    data = []
    for i in range(len(course_names)):
        data.append([str(course_names[i]), str(exam_avgs_set[i])])
    # model = CourseListing
    # field_names = [f.name for f in model._meta.get_fields()]
    # data = [[getattr(ins, name) for name in field_names]
    #         for ins in Model.objects.prefetch_related().all()]
    print(data)
    return render(request, 'browse.html', {'field_names': field_names, 'data': data, 'depts': depts})