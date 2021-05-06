from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'budget', 'notes']
        # widgets = {'home': forms.HiddenInput()}
