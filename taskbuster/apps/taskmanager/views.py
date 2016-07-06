from django.shortcuts import render, get_object_or_404
from .models import Project, Task, Profile
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm, TaskForm


named_objects = {}


@login_required
def project_list(request):
    load_plugin()
    projects = Project.objects.all().order_by('name')
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})


def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = Profile.objects.filter(user=request.user).first()
            project.save()
            projects = Project.objects.all().order_by('name')
            return render(request, "taskmanager/tasks_list.html", {
                'projects': projects})
    else:
        form = ProjectForm()
    return render(request, "taskmanager/add_project.html", {'form': form})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskmanager/tasks_list.html', {'task': task})


@login_required
def close_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.percentage = "100"
    task.save()
    projects = Project.objects.all().order_by('name')
    named_objects['tweet_task'](task.name)
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})


@login_required
def close_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.closed = True
    project.save()
    tasks = Task.objects.filter(project=project)
    for task in tasks:
        task.percentage = "100"
        task.save()
    projects = Project.objects.all().order_by('name')
    named_objects['tweet_project'](project.name)
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})


def load_plugin():
    from pkg_resources import iter_entry_points
    for entry_point in iter_entry_points(group='twitter.plugin'):
        named_objects.update({entry_point.name: entry_point.load()})
