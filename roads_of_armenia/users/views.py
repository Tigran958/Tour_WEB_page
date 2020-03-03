from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse

from .forms import CollectionTitleFormSet, CustomUserForm
from .models import User


class StudentSignUpView(CreateView):
    model = User
    form_class = CustomUserForm
    template_name = 'users/signup.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'driver'
    #     return super().get_context_data(**kwargs)
    def get_context_data(self, **kwargs):
        data = super(StudentSignUpView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(self.request.POST)
        else:
            data['titles'] = CollectionTitleFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context["titles"]
        self.object = form.save()
        if titles.is_valid():
            titles.instance = self.object
            titles.save()
        return super().form_valid(form)

    def get_success_url(self):
        return redirect("/")
