from django.urls import path
from base import views
urlpatterns = [
    path('', views.index, name='index'),
    path('save_student', views.save_student, name='save_student'),
    path('delete_student', views.delete_student, name='delete_student'),
    path("edit_student", views.edit_student, name='edit_student'),
]