from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('demand', views.demand),
    path('geography', views.geography),
    path('skills', views.skills),
    path('vacancies', views.vacancies),
]
