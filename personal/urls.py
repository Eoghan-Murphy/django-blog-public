from django.urls import path

from . import views

app_name = 'personal'
urlpatterns = [
    path('', views.index, name='index'),
]
