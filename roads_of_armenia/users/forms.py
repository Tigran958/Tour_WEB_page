from django import forms
from .models import User, Driver, Guide, Client, TourAgents, Tour, TourImage
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .choices import USER_CHOICES, LANGUAGES_CHOICES

class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        # fields = ['username', 'email', 'bank_account', 'name', 'phone_number','user_choices']
        fields = ['email','user_choices']
        widgets = {'user_choices': forms.HiddenInput()}


class DriverUserCreationForm(ModelForm):

    class Meta:
        model = Driver
        fields = '__all__'
        # fields = ['*']


CollectionTitleFormSet = inlineformset_factory(
    User, Driver, form=DriverUserCreationForm,
    fields='__all__', extra=1, can_delete=True
)

class ClientUserCreationForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        # fields = ['*']


CollectionTitleFormSetClient = inlineformset_factory(
    User, Client, form=ClientUserCreationForm,
    fields='__all__', extra=1, can_delete=True
)

class GuideUserCreationForm(ModelForm):

    class Meta:
        model = Guide
        fields = '__all__'
        # fields = ['*']


CollectionTitleFormSetGuide = inlineformset_factory(
    User, Guide, form=GuideUserCreationForm,
    fields='__all__', extra=1, can_delete=True
)


class TourAgentsUserCreationForm(ModelForm):

    class Meta:
        model = TourAgents
        fields = '__all__'


CollectionTitleFormSetTourAgents = inlineformset_factory(
    User, TourAgents, form=TourAgentsUserCreationForm,
    fields='__all__', extra=1, can_delete=True
)

class TourCreationForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'
        widgets = {'tour': forms.HiddenInput()}

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username',]
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class GuideForm(ModelForm):
    class Meta:
        model = Guide
        fields = ['name',]
    name = forms.CharField(required=False)
    language = forms.ChoiceField(choices=LANGUAGES_CHOICES, required=False)
