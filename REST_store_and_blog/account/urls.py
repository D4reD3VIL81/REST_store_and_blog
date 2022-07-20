from django.urls import path
from django.urls import include
from .views import DashboardView
from .views import AccountCreationFormView

app_name = 'account'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profiles/', include('django.contrib.auth.urls')),
    path('register/', AccountCreationFormView.as_view(), name='register')
]