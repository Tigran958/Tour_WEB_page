from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse

from .forms import CollectionTitleFormSet, CustomUserForm , CollectionTitleFormSetClient, CollectionTitleFormSetGuide, CollectionTitleFormSetTourAgents 
from .models import User


def home(request):
    return render(request, 'users/reg_home.html')


class UserSignUpView(CreateView):
    model = User
    form_class = CustomUserForm
    template_name = 'users/signup.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'driver'
    #     return super().get_context_data(**kwargs)
    def get_context_data(self, **kwargs):
        filter_key = self.kwargs['key']
        filter_dict = {'1':CollectionTitleFormSet, '2': CollectionTitleFormSetClient,
                        '3': CollectionTitleFormSetGuide, '4': CollectionTitleFormSetTourAgents
                    }
        
        user_coll_type = filter_dict[str(filter_key)]

        def filter_type(TitleFormSet):  
            data = super(UserSignUpView, self).get_context_data(**kwargs)
            if self.request.POST:
                data['titles'] = TitleFormSet(self.request.POST)
            else:
                data['titles'] = TitleFormSet()
            return data    

        data = filter_type(user_coll_type)

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
