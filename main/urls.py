from django.urls import path
from .views import index, timetable, add_hw, delete


urlpatterns = [
    path('', index, name="main"),
    path('timetable/', timetable, name="timetable"),
    path('add_hw/', add_hw, name="add_hw"),
    path('delete/<int:pk>/', delete),
]