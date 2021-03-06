from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Home(models.Model):
    nickname = models.CharField(max_length=40, default="NA")
    address = models.CharField(max_length=40, default="NA")
    city = models.CharField(max_length=20, default="NA")
    state = models.CharField(max_length=20, default="NA")
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    square_feet = models.IntegerField(default=0)
    year_built = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('homes_detail', kwargs={'home_id': self.id})


class Project(models.Model):
    name = models.CharField(max_length=20, default="NA")
    budget = models.IntegerField(default=0)
    notes = models.CharField(max_length=200, default="NA")
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={"project_id": self.id})


class Contacts(models.Model):
    name = models.CharField(max_length=20, default="NA")
    phone = models.BigIntegerField(default=1111111111)
    business = models.CharField(max_length=40, default="NA")
    service = models.CharField(max_length=30, default="NA")
    notes = models.CharField(max_length=200, default="NA")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('contacts_detail', kwargs={"contact_id": self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for project_id: {self.project_id} @{self.url}"


class Budget(models.Model):
    date = models.DateField(null=True)
    company = models.CharField(max_length=40, default=" ")
    description = models.CharField(max_length=200, default=" ")
    cost = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=40, default=" ")
