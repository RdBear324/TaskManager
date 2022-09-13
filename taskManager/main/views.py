from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    task = Task.objects.all()
    return render(request, 'index.html', {'title': 'Главная страница', 'tasks': task})


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')
