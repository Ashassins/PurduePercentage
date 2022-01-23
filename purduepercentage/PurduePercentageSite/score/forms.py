from django import forms
from django.utils.safestring import mark_safe

class ScoreForm(forms.Form):
    your_course = forms.CharField(label='Your Course', max_length=100, widget= forms.TextInput(attrs={'placeholder':'ECE 101010'}))
    your_score = forms.IntegerField(label=mark_safe('Your Score'))
    your_grade = forms.CharField(label='Your Overall Grade', max_length=1)