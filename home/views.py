from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'registration/profile.html')



#in settings.py last