from django.urls import path
from . import views

urlpatterns = [
    # base urls / others
    path('', views.home, name='home'),

    # home urls
    path('homes/create/', views.Create_Home.as_view(), name='create_home'),
    path('homes/<int:pk>/update/', views.Update_Home.as_view(), name='update_home'),
    path('homes/<int:pk>/delete/', views.Delete_Home.as_view(), name='delete_home'),
    path('homes/', views.homes_index, name='homes_index'),
    path('homes/<int:home_id>', views.homes_detail, name='homes_detail'),

    # project urls
    path('projects/create/', views.Create_Project.as_view(), name='create_project'),
    path('projects/<int:pk>/update/',
         views.Update_Project.as_view(), name='update_project'),
    path('projects/<int:pk>/delete/',
         views.Delete_Project.as_view(), name='delete_project'),
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<int:project_id>',
         views.projects_detail, name='project_detail'),

    # contact urls
    path('contacts/create/', views.Create_Contact.as_view(), name='create_contact'),
    path('contacts/<int:pk>/update/',
         views.Update_Contact.as_view(), name='update_contact'),
    path('contacts/<int:pk>/delete/',
         views.Delete_Contact.as_view(), name='delete_contact'),
    path('contacts/<int:contact_id>',
         views.contacts_detail, name='contacts_detail'),

]
