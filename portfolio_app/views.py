from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.order_by('id')
    return render(request, 'home.html', {'projects': projects})