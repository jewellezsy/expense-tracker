from django.urls import path
from . import views

urlpatterns = [
    path('delete_expense/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
]
