from django import forms
from django.utils.safestring import mark_safe

class ScoreForm(forms.Form):
    your_score = forms.IntegerField(label=mark_safe('Your Score'))
    your_grade = forms.CharField(label='Your Overall Grade', max_length=1)