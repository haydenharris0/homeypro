# Generated by Django 3.2 on 2021-05-01 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_home_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='home',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.home'),
        ),
    ]
