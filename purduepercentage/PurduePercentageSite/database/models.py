from typing import List, Optional
from django.conf import settings
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import BooleanField, FloatField, IntegerField
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy

class ExamType(TextChoices):
    MIDTERM_1 = "M1", gettext_lazy("MIDTERM_1")
    MIDTERM_2 = "M2", gettext_lazy("MIDTERM_2")
    MIDTERM_3 = "M3", gettext_lazy("MIDTERM_3")
    MIDTERM_4 = "M4", gettext_lazy("MIDTERM_4")
    FINAL = "FN", gettext_lazy("FINAL")


class StudyType(TextChoices):
    REWATCH = "RW", gettext_lazy("REWATCH")
    NOTES = "NT", gettext_lazy("NOTES")
    PRACTICE = "PR", gettext_lazy("PRACTICE")
    TEXTBOOK = "TB", gettext_lazy("TEXTBOOK")
    FLASHCARDS = "FC", gettext_lazy("FLASHCARDS")
    OTHER = "OT", gettext_lazy("OTHER")


class Lifestyle(TextChoices):
    SEDENTARY = "SE", gettext_lazy("SEDENTARY")
    MODERATE = "MO", gettext_lazy("MODERATE")
    ACTIVE = "AC", gettext_lazy("ACTIVE")

class LetterGrade(TextChoices):
    A = "A", gettext_lazy("A")
    B = "B", gettext_lazy("B")
    C = "C", gettext_lazy("C")
    D = "D", gettext_lazy("D")
    F = "F", gettext_lazy("F")


class CourseListing(Model):
    department = CharField(max_length=255)
    course_number = CharField(max_length=255)
    course_title = CharField(max_length=255, null=True)

    def __str__(self) -> str:
        rv = f"<Course: {self.department}-{self.course_number}"
        if title := self.course_title:
            rv += f" ({title})"
        rv += ">"
        return rv

class Professor(Model):
    department = CharField(max_length=255)
    first = CharField(max_length=255)
    last = CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first} {self.last}"

class TeachingAssistant(Model):
    department = CharField(max_length=255)
    first = CharField(max_length=255)
    last = CharField(max_length=255)

class StudyMethod(Model):
    method = CharField(max_length=2, choices=StudyType.choices, default=StudyType.OTHER)

class Exam(Model):
    course = ForeignKey(CourseListing, on_delete=CASCADE)
    exam = CharField(max_length=2, choices=ExamType.choices, default=ExamType.MIDTERM_1)
    year = IntegerField(null=True)
    score = FloatField()
    letter_grade = CharField(max_length=2 , choices=LetterGrade.choices, default=LetterGrade.A)
    professor = ForeignKey(Professor, on_delete=CASCADE, null=True)
    ta = ForeignKey(TeachingAssistant, on_delete=CASCADE, null=True)
    lec_attendance = BooleanField()
    rec_attendance = BooleanField()
    study_method = ForeignKey(StudyMethod, on_delete=CASCADE, null=True)
    hrs_study = IntegerField()
    major = CharField(max_length=255, null=True)
    minor = CharField(max_length=255, null=True)
    avg_sleep = IntegerField(null=True)
    extracurricular_hours = IntegerField(null=True)
    musician = BooleanField(null=True)
    artist = BooleanField(null=True)
    athlete = BooleanField(null=True)
    lifestyle = CharField(
        max_length=2, choices=Lifestyle.choices, default=Lifestyle.MODERATE, null=True
    )
    num_semesters = IntegerField(null=True)
    coop = BooleanField()
    retake = BooleanField()

    def __str__(self) -> str:
        return f"<Exam: course={self.course}, exam={self.exam}, score={self.score}>"


def get_prof_for_dep(dep: str) -> List[str]:
    return list(map(lambda p: str(p), Professor.objects.all()))

def create_course(department: str, number: int, title: Optional[str] = None):
    if not CourseListing.objects.filter(department=department, course_number=number):
        c = CourseListing(department=department, course_number=number, course_title=title)
        c.save()

def create_exam(course: CourseListing, score: float):
    e = Exam(course=course, score=score)
    e.save()

def get_all_courses() -> List[CourseListing]:
    return CourseListing.objects.all()

def get_departments() -> List[str]:
    return list(set(map(lambda course: course.department, CourseListing.objects.all())))

def get_course(department: str, number: int) -> Optional[CourseListing]:
    return CourseListing.objects.get(department=department, number=number)

def get_exams_for_course(course: CourseListing) -> List[Exam]:
    return Exam.objects.filter(course=course)
