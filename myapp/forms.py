from django import forms
from .models import JournalRecord
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class JournalRecordForm(forms.ModelForm):

    class Meta:
        model = JournalRecord
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
