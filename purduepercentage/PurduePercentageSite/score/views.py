from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ScoreForm

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
            print("Got Post Request")
            print(form.cleaned_data['your_score'])
            print(form.cleaned_data['your_grade'])
            return HttpResponseRedirect('/pphomepage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScoreForm()

    return render(request, 'score.html', {'form': form})