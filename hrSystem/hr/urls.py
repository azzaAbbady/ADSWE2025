from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_add, name='department_add'),
    path('departments/edit/<int:pk>/', views.department_edit, name='department_edit'),
    path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),
    
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('api/employees/add/',views.add_employee_api, name='add_employee_api'),
    path('employees/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('departments/<int:pk>/employees/', views.department_employees, name='department_employees'),
]
