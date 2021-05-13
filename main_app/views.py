from main_app.forms import BudgetForm, ProjectForm
from django.shortcuts import render
from .models import Budget, Contacts, Home, Project, Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
import uuid
import boto3

S3_BASE_URL = '.s3.amazonaws.com/'

BUCKET = 'homeypro'


# ----- Base view's & profile -----


def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    homes = Home.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    contacts = Contacts.objects.filter(user=request.user)
    context = {
        'homes': homes,
        'projects': projects,
        'contacts': contacts,
    }

    return render(request, 'profile/profile.html', context)


# -----Home views-----


class Create_Home(LoginRequiredMixin, CreateView):
    model = Home
    fields = [
        'nickname', 'address', 'city', 'state', 'bedrooms',
        'bathrooms', 'square_feet', 'year_built'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class Update_Home(LoginRequiredMixin, UpdateView):
    model = Home
    fields = [
        'nickname', 'address', 'city', 'state', 'bedrooms',
        'bathrooms', 'square_feet', 'year_built'
    ]


class Delete_Home(LoginRequiredMixin, DeleteView):
    model = Home
    success_url = '/homes'


@login_required
def homes_index(request):
    homes = Home.objects.filter(user=request.user)
    context = {'homes': homes}

    return render(request, 'homes/index.html', context)


@login_required
def homes_detail(request, home_id):
    home = Home.objects.get(id=home_id)
    projects = Project.objects.filter(user=request.user)
    contacts = Contacts.objects.filter(user=request.user)
    project_form = ProjectForm()
    context = {
        'home': home,
        'projects': projects,
        'contacts': contacts,
        'project_form': project_form
    }

    return render(request, 'homes/detail.html', context)


# -----Project views-----

class Create_Project(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'budget', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


@login_required
def add_project(request, home_id):
    form = ProjectForm(request.POST)

    if form.is_valid():
        new_project = form.save(commit=False)
        new_project.home_id = home_id
        form.instance.user = request.user
        new_project.save()

    return redirect('homes_detail', home_id=home_id)


class Update_Project(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'budget', 'notes', 'start_date', 'end_date']


class Delete_Project(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/homes'


@login_required
def projects_index(request):
    projects = Project.objects.filter(user=request.user)
    context = {'projects': projects}

    return render(request, 'projects/index.html', context)


@login_required
def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {'project': project}

    return render(request, 'projects/detail.html', context)


# -----Contact Views-----


class Create_Contact(LoginRequiredMixin, CreateView):
    model = Contacts
    fields = ['name', 'phone', 'business', 'service', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class Update_Contact(LoginRequiredMixin, UpdateView):
    model = Contacts
    fields = ['name', 'phone', 'business', 'service', 'notes']


class Delete_Contact(LoginRequiredMixin, DeleteView):
    model = Contacts
    success_url = '/homes'


@login_required
def contacts_detail(request, contact_id):
    contact = Contacts.objects.get(id=contact_id)
    context = {'contact': contact}

    return render(request, 'contacts/detail.html', context)

# -----Auth-----


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}

    return render(request, 'registration/signup.html', context)

# ----- Photo upload & views -----


@login_required
def add_photo(request, project_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            # ------------------------------------------------------
            # url = f"{S3_BASE_URL}{BUCKET}/{key}"
            url = f"https://{BUCKET}{S3_BASE_URL}{key}"
            photo = Photo(url=url, project_id=project_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')

    return redirect('project_detail', project_id=project_id)


@login_required
def photos_index(request):
    homes = Home.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    photo = Photo.objects.all()
    context = {'homes': homes, 'projects': projects, 'photo': photo}

    return render(request, 'profile/photos.html', context)


@login_required
def budget(request):
    homes = Home.objects.filter(user=request.user)
    budget = Budget.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    budget_form = BudgetForm()
    sum_of_expenses = Budget.objects.filter(
        user=request.user).aggregate(Sum("cost"))
    context = {
        'homes': homes,
        'budget': budget,
        'projects': projects,
        'budget_form': budget_form,
        'sum_of_expenses': sum_of_expenses
    }

    return render(request, 'profile/budget.html', context)


@login_required
def add_budget(request):
    form = BudgetForm(request.POST)

    if form.is_valid():
        new_budget = form.save(commit=False)
        form.instance.user = request.user
        new_budget.save()

    return redirect('budget')


class Update_Budget(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ['date', 'company', 'description', 'cost', 'house']
    success_url = '/profile/budget/'


class Delete_Budget(LoginRequiredMixin, DeleteView):
    model = Budget
    success_url = '/profile/budget/'
