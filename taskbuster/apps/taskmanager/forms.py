from django import forms
from .models import Project
from .models import Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name',)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'percentage',)
