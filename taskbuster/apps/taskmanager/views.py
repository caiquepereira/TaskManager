from django.shortcuts import render, get_object_or_404
from .models import Project, Task
from django.contrib.auth.decorators import login_required


@login_required
def project_list(request):

    from pkg_resources import iter_entry_points
    named_objects = {}
    for entry_point in iter_entry_points(group='image.plugin'):
        named_objects.update({entry_point.name: entry_point.load()})
        # print(named_objects)
    named_objects['jpg_image']("teste")
    named_objects['png_image']()

    projects = Project.objects.all().order_by('name')
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskmanager/tasks_list.html', {'task': task})


def close_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.percentage = "100"
    task.save()
    projects = Project.objects.all().order_by('name')
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})


def close_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    print project
    print tasks
    for task in tasks:
        task.percentage = "100"
        task.save()
    projects = Project.objects.all().order_by('name')
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})
