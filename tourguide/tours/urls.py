from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('tours/', views.tours, name='tours'),
    path('tours/details/<int:id>', views.details, name='details')
]
