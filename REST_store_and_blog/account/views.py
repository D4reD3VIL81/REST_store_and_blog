from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import AccountCreationForm

# Create your views here.

class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'
    
class AccountCreationFormView(FormView):
    template_name = 'account/register.html'
    form_class = AccountCreationForm
    success_url = reverse_lazy('account:dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        print(user)
        user.save()

        return super().form_valid(form)
