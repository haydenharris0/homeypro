from django.shortcuts import render
from .models import Home, Project
from django.views.generic.edit import CreateView


def home(request):
    return render(request, 'home.html')

# -----Home views-----


class Create_Home(CreateView):
    model = Home
    fields = ['nickname', 'address', 'city', 'state']
    success_url = '/homes/'


class Update_Home(CreateView):
    model = Home
    fields = ['nickname', 'address', 'city', 'state']
    success_url = '/homes_detail/'


def homes_index(request):
    homes = Home.objects.all()
    context = {'homes': homes}
    return render(request, 'homes/index.html', context)


def homes_detail(request, home_id):
    home = Home.objects.get(id=home_id)
    context = {'home': home}
    return render(request, 'homes/detail.html', context)

# -----Project views-----


class Create_Project(CreateView):
    model = Project
    fields = ['name', 'budget', 'notes']
    success_url = '/homes/'


class Update_Project(CreateView):
    model = Project
    fields = ['name', 'budget', 'notes']
    success_url = '/homes/'


def projects_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)


def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'projects/detail.html', context)
