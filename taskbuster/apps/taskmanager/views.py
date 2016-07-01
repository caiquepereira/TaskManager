from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def post_list(request):

    from pkg_resources import iter_entry_points
    for entry_point in iter_entry_points(group='cms.plugin', name=None):
        print(entry_point)

    from pkg_resources import iter_entry_points
    available_methods = []
    for entry_point in iter_entry_points(group='authkit.method', name=None):
        available_methods.append(entry_point.load())

    projects = Project.objects.all().order_by('name')
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})
