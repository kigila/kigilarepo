from django.shortcuts import render
from project.models import Project

# Create your views here.


def project_index(request):
    projects = Project.objects.all()
    featured_project = Project.objects.get(pk=len(projects))
    context = {
        'projects': projects,
        'featured_project':featured_project,
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)
