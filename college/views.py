from django.shortcuts import render
from .models import Courses

# Create your views here.

def get(request):
    data = Courses.objects.all()
    context = {"courses": data}
    return render(request, 'index.html', context)
