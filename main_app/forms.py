from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import Project
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'budget', 'notes', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
