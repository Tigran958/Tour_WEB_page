from django.contrib.auth import login,logout
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse

from .forms import CollectionTitleFormSet, CustomUserForm , CollectionTitleFormSetClient, CollectionTitleFormSetGuide, CollectionTitleFormSetTourAgents 
from .models import User, Driver, CarImageModel, Guide, TourAgents


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
        return 'reg_home'

def client_page(request):
    return render(request, 'users/client_page.html')

def driver_list(request):
    drivers = Driver.objects.all().prefetch_related("aa")
    print(drivers[0].aa.__dict__)

    context = {'drivers':drivers}

    return render(request, 'users/driver_list.html', context)

def guide_list(request):
    guides = Guide.objects.all()

    context = {'guides':guides}

    return render(request, 'users/guide_list.html', context)  

def agent_list(request):
    agents = TourAgents.objects.all()

    context = {'agents':agents}

    return render(request, 'users/agents_list.html', context)  


def login_1(request):
    return redirect('up/client_page')

def u_logout(request):
    logout(request)
    return redirect('/sign/up/client_page')