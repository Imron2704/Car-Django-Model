from django.urls import path, re_path
from .views import edit_cars, index, contacts, get_cars, find_by_name, get_1, get_2, get_3, get_4, get_5, get_6, get_7, get_8, get_9, get_10

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('cars/', get_cars),
    path('cars/1',get_1),
    path('cars/2', get_2),
    path('cars/3', get_3),
    path('cars/4', get_4),
    path('cars/5',get_5),
    path('cars/6',get_6),
    path('cars/7',get_7),
    path('cars/8',get_8),
    path('cars/9',get_9),
    path('cars/10',get_10),
    path('cars/edit/', edit_cars),
    path('cars/<int:id>', get_cars),
    path('cars/<slug:text>', find_by_name),
    # re_path('regions/$', find_by_name),
]
