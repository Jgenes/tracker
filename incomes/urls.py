# userAuth/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('income/', views.income, name="income"), 
    path('addIncome/', views.addIncome, name="addIncome"),
    path('deleteIncome/<int:id>/', views.deleteIncome, name='deleteIncome'),
    path('editIncome/<int:id>/', views.editIncome, name='editIncome'),  # Add this line

    # path('dashboard/', views.dashboard, name="dashboard"),
    # This is your index page handled by the userAuth app
]
