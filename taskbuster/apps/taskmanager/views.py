from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def post_list(request):

    from pkg_resources import iter_entry_points
    named_objects = {}
    for entry_point in iter_entry_points(group='image.plugin'):
        named_objects.update({entry_point.name: entry_point.load()})
        print(named_objects)
    named_objects['jpg_image']()
    named_objects['png_image']()

    projects = Project.objects.all().order_by('name')
    return render(request, "taskmanager/tasks_list.html", {
        'projects': projects})
