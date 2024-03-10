from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.driver_list, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path("driver-info/<int:driver_id>", views.driver_info, name="driver_info"),
    path("add-driver/", views.add_driver, name="add_driver"),
    path("companies/", views.companies_list, name="companies"),
    path("companies/company-info/<int:company_id>", views.company_info, name="company_info"),
    path("companies/add-company/", views.add_company, name="add_company")
]