from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='tracker-home'),
    path('Tracker/addItem',views.addItem, name ='tracker-addItem'),
    path('Tracker/removeItem',views.removeItem, name ='tracker-removeItem'),
]