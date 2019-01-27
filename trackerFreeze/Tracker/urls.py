from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='tracker-home'),
    path('Tracker/addItem',views.addItem, name ='tracker-addItem'),
    path('Tracker/fridgeContent',views.fridgeContent, name ='tracker-fridgeContent'),
    path('Tracker/addItem_submission',views.addItem_submission, name ='tracker-addItem_submission'),
    path('Tracker/removeItem',views.removeItem, name ='tracker-removeItem'),
]