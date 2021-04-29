from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=20, default="NA")
    budget = models.IntegerField(default=0)
    notes = models.CharField(max_length=200, default="NA")

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={"project_id": self.id})


class Home(models.Model):
    nickname = models.CharField(max_length=40, default="NA")
    address = models.CharField(max_length=40, default="NA")
    city = models.CharField(max_length=20, default="NA")
    state = models.CharField(max_length=20, default="NA")
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    square_feet = models.IntegerField(default=0)
    year_built = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('homes_detail', kwargs={'home_id': self.id})


class Contacts(models.Model):
    name = models.CharField(max_length=20, default="NA")
    number = models.IntegerField(default=0)
    business = models.CharField(max_length=40, default="NA")
    service = models.CharField(max_length=30, default="NA")
    notes = models.CharField(max_length=200, default="NA")
