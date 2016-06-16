from django.shortcuts import render
from .models import Project


def post_list(request):

    projects = Project.objects.all().order_by('name')
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})
