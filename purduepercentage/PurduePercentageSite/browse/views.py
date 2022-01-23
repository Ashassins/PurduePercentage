from django.shortcuts import render

# Create your views here.
def browse(request):
    return render(request, 'browse.html')