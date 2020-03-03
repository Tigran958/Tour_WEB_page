from django import forms
from .models import User, Driver
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory
from django.forms import ModelForm


class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'bank_account', 'name', 'phone_number']


class DriverUserCreationForm(ModelForm):

    class Meta:
        model = Driver
        fields = '__all__'
        # fields = ['*']


CollectionTitleFormSet = inlineformset_factory(
    User, Driver, form=DriverUserCreationForm,
    fields='__all__', extra=1, can_delete=True
)
