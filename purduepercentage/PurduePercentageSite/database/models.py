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
    MIDTERM_1 = 'M1', gettext_lazy('MIDTERM_1')
    MIDTERM_2 = 'M2', gettext_lazy('MIDTERM_2')
    MIDTERM_3 = 'M3', gettext_lazy('MIDTERM_3')
    MIDTERM_4 = 'M4', gettext_lazy('MIDTERM_4')
    FINAL = 'FN', gettext_lazy('FINAL')

class StudyType(TextChoices):
    REWATCH = "RW", gettext_lazy("REWATCH")
    NOTES = "NT", gettext_lazy("NOTES")
    PRACTICE = "PR", gettext_lazy("PRACTICE")
    TEXTBOOK = "TB", gettext_lazy("TEXTBOOK")
    FLASHCARDS = "FC", gettext_lazy("FLASHCARDS")
    OTHER = "OT", gettext_lazy("OTHER")

class Lifestyle(TextChoices):
    SEDENTARY = 'SE', gettext_lazy('SEDENTARY')
    MODERATE = 'MO', gettext_lazy('MODERATE')
    ACTIVE = 'AC', gettext_lazy('ACTIVE')

class CourseListing(Model):
    department = CharField(max_length=255)
    course_number = CharField(max_length=255)
    course_title = CharField(max_length=255)

class Professor(Model):
    department = CharField(max_length=255)
    first = CharField(max_length=255)
    last = CharField(max_length=255)

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
    lifestyle = CharField(max_length=2, choices=Lifestyle.choices, default=Lifestyle.MODERATE, null=True)
    num_semesters = IntegerField(null=True)
    coop = BooleanField()
    retake = BooleanField()
