from django.urls import path

from employee.views import index, add, updateEmployee, deleteEmployee

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('update/<int:pk>/', updateEmployee, name='update'),
    path('delete/<int:pk>/', deleteEmployee, name='delete'),
]
