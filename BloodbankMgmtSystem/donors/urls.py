from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.main, name='main'),
    path('donors/', views.donors, name='donors'),
    path('donors/details/<int:id>', views.details, name='details'),

]
