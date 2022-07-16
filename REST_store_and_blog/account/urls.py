from django.urls import path
from django.urls import include
from .views import DashboardView

app_name = 'account'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profiles/',include('django.contrib.auth.urls'))
]