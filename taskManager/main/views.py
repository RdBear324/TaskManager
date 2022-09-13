from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    task = Task.objects.order_by('-create_on')
    context = {'title': 'Главная страница',
               'tasks': task
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def create(request):
    return render(request, 'create.html')
