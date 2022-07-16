from pyexpat import model
from .models import AccountModel
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = AccountModel
        fields = ("email", "name")