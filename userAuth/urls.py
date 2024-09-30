

# userAuth/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('signUp/', views.signUp, name="signUp"),
    path('dashboard/', views.dashboard, name="dashboard"),
     # This is your index page handled by the userAuth app
]
