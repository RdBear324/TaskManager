from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "author", "task"]
        widgets = {
            'title': TextInput(attrs={"class": 'form-control', 'placeholder' : 'Введите название'}),
            'author': TextInput(attrs={"class": 'form-control', 'placeholder': 'Введите автора'}),
            'task': Textarea(attrs={"class": 'form-control', 'placeholder': 'Введите задачу'}),

        }