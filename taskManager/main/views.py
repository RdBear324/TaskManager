from django.shortcuts import render, redirect
from .forms import TaskForm
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
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка! Неверная форма!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)
