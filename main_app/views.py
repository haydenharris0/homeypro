from django.shortcuts import render
from .models import Contacts, Home, Project
from django.views.generic.edit import CreateView, DeleteView, UpdateView


def home(request):
    return render(request, 'home.html')


# -----Home views-----


class Create_Home(CreateView):
    model = Home
    fields = ['nickname', 'address', 'city', 'state',
              'bedrooms', 'bathrooms', 'square_feet', 'year_built']


class Update_Home(UpdateView):
    model = Home
    fields = ['nickname', 'address', 'city', 'state',
              'bedrooms', 'bathrooms', 'square_feet', 'year_built']


class Delete_Home(DeleteView):
    model = Home


def homes_index(request):
    homes = Home.objects.all()
    context = {'homes': homes}
    return render(request, 'homes/index.html', context)


def homes_detail(request, home_id):
    home = Home.objects.get(id=home_id)
    projects = Project.objects.all()
    contacts = Contacts.objects.all()
    context = {'home': home, 'projects': projects, 'contacts': contacts}
    return render(request, 'homes/detail.html', context)


# -----Project views-----


class Create_Project(CreateView):
    model = Project
    fields = ['name', 'budget', 'notes']


class Update_Project(UpdateView):
    model = Project
    fields = ['name', 'budget', 'notes']


class Delete_Project(DeleteView):
    model = Project
    success_url = '/homes'


def projects_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)


def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    homes = Home.objects.all()
    context = {'project': project, 'homes': homes}
    return render(request, 'projects/detail.html', context)


# -----Contact Views-----


class Create_Contact(CreateView):
    model = Contacts
    fields = ['name', 'number', 'business', 'service', 'notes']


class Update_Contact(UpdateView):
    model = Contacts
    fields = ['name', 'number', 'business', 'service', 'notes']


class Delete_Contact(DeleteView):
    model = Contacts
    success_url = '/homes'


def contacts_detail(request, contact_id):
    contact = Contacts.objects.get(id=contact_id)
    context = {'contact': contact}
    return render(request, 'contacts/detail.html', context)
