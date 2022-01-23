from django.shortcuts import render
from database.models import *

# Create your views here.
def browse(request):
    field_names = ['Course Code', 'Exam Average']
    courses = get_all_courses()
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
    return render(request, 'browse.html', {'field_names': field_names, 'data': data})