from django.db import models
from django.conf import settings
from django.db.models.base import Model

from django.db.models.enums import TextChoices
from django.db.models.fields import BooleanField, IntegerField, FloatField
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


class StudyMethod(Model):
    method = CharField(max_length=2, choices=StudyType.choices, default=StudyType.OTHER)

class Exam(Model):
    course = CharField(max_length=255, default=False)
    exam = CharField(max_length=2, choices=ExamType.choices, default=ExamType.MIDTERM_1)
    score = FloatField()
    professor = CharField(max_length=255)
    ta = CharField(max_length=255)
    lec_attendance = BooleanField()
    rec_attendance = BooleanField()
    study_method = ForeignKey(StudyMethod, on_delete=models.CASCADE)
    hrs_study = IntegerField()
    major = CharField(max_length=255)
    minor = CharField(max_length=255)
    avg_sleep = IntegerField()
    extracurricular_hours = IntegerField()
    musician = BooleanField()
    artist = BooleanField()
    athlete = BooleanField()
    lifestyle = CharField(max_length=2, choices=Lifestyle.choices, default=Lifestyle.MODERATE)
    num_semesters = IntegerField()
    coop = BooleanField()
    retake = BooleanField()
