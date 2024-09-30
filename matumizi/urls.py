# userAuth/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name="list"), 
    path('addMatumizi/', views.addMatumizi, name="addMatumizi"),
    path('deleteMatumizi/<int:id>/', views.deleteMatumizi, name='deleteMatumizi'),
    path('editMatumizi/<int:id>/', views.editMatumizi, name='editMatumizi'),  # Add this line

    # path('dashboard/', views.dashboard, name="dashboard"),
    # This is your index page handled by the userAuth app
]
