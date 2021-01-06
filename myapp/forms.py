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

    # def __init__(self, *args, **kwargs):
    #     super(CreasteUserForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'


# class ContactForm(forms.Form):
#     size = forms.CharField()
#     species = forms.ChoiceField(choices=[
#     ('fish', 'Chum'),
#     ('fish', 'Coho'),
#     ('fish', 'Chinook'),
#     ('fish', 'Pink'),
#     ('fish', 'Sockeye'),
#     ('fish', 'Trout')
#     ])
#     location = forms.CharField()
#     date = forms.CharField()
#     method = forms.CharField(widget=forms.Textarea)
