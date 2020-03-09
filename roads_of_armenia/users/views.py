from django.contrib.auth import login,logout
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse

from .forms import CollectionTitleFormSet, CustomUserForm , CollectionTitleFormSetClient, CollectionTitleFormSetGuide, CollectionTitleFormSetTourAgents 
from .models import User, Driver, CarImageModel, Guide, TourAgents
<<<<<<< HEAD
from .filters import DriverFilter, TourAgentsFilter, GuideFilter
from django.db.models.functions import Substr
=======
from .filters import DriverFilter

>>>>>>> 35feef372f96249c469cc6f81008ce235f98bae1

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

<<<<<<< HEAD
=======

>>>>>>> 35feef372f96249c469cc6f81008ce235f98bae1
    drivers = Driver.objects.all().prefetch_related("aa")
    # print(drivers[0].aa.__dict__)
    driver_filter = DriverFilter(request.GET, queryset=drivers)
    
<<<<<<< HEAD
    try:
        name = request.GET['DriverSearch']
    except:
        name = {"DriverSearch":[]}

    if name:
        drivers = driver_filter.qs.filter(user__name__contains=F"{name}")
    else:
        drivers = driver_filter.qs

    if not drivers.exists():
        print(drivers) 
        # print(request.GET.__dict__)     
        drivers = Driver.objects.all().prefetch_related("aa")
        print(drivers)

    #TODO There can be used __range
    
    context = {'drivers':drivers, 'driver_filter': driver_filter}
=======
    name = request.GET['DriverSearch']

    if name:
        drivers = driver_filter.qs.filter(user__name=name)
    else:
        drivers = driver_filter.qs

    context = {'drivers':drivers, 'driver_filter': driver_filter} 
         
>>>>>>> 35feef372f96249c469cc6f81008ce235f98bae1

    return render(request, 'users/driver_list.html', context)



def guide_list(request):
    guides = Guide.objects.all()

<<<<<<< HEAD
    guide_filter = GuideFilter(request.GET, queryset=guides)
    
    try:
        name = request.GET['GuideSearch']
    except:
        name = {"GuideSearch":[]}

    if name:
        guides = guide_filter.qs.filter(user__name=F"{name}")
    else:
        guides = guide_filter.qs

    # print(guide_filter.qs.__dict__)


    context = {'guides':guides, 'guide_filter':guide_filter}
=======
    context = {'guides':guides}
>>>>>>> 35feef372f96249c469cc6f81008ce235f98bae1

    return render(request, 'users/guide_list.html', context)  

def agent_list(request):
    agents = TourAgents.objects.all()

<<<<<<< HEAD
    agent_filter = TourAgentsFilter(request.GET, queryset=agents)
    

    def func_valid_input(key):
        try:
            name = request.GET[key]
        except:
            name = {key:[]}
        return name

    name = func_valid_input('AgentSearch')
    price_start = func_valid_input('PriceStart')    
    price_to = func_valid_input('PriceTo')    
    date_start = func_valid_input('DateStart')   
    date_end = func_valid_input('DateEnd')   


    if name:
        agents = agent_filter.qs.filter(user__name__contains=F"{name}", 
                                        # date_of_tour__range=(date_start,date_end),
                                        )
    else:
        agents = agent_filter.qs
     
                                        # first_to_ten_price__range=(price_start,price_to)
    # if not agents.exists(): 
    #     # print(request.GET.__dict__)     
    #     agents = TourAgents.objects.all()



    context = {'agents':agents, 'agent_filter': agent_filter} 

=======
    context = {'agents':agents}
>>>>>>> 35feef372f96249c469cc6f81008ce235f98bae1

    return render(request, 'users/agents_list.html', context)  


def login_1(request):
    return redirect('up/client_page')

def u_logout(request):
    logout(request)
    return redirect('/sign/up/client_page')


def driver_search(request):

    if request.method == 'POST':
        print(request__dict__)

    return render(request, 'users/driver_search.html')     