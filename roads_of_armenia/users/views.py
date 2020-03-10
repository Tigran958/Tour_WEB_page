from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse

from .forms import * # CollectionTitleFormSet, CustomUserForm , CollectionTitleFormSetClient, CollectionTitleFormSetGuide, CollectionTitleFormSetTourAgents 
from .models import User, Driver, CarImageModel, Guide, TourAgents, Tour

from .filters import DriverFilter, TourAgentsFilter, GuideFilter, TourFilter
import datetime


def home(request):
    return render(request, 'users/reg_home.html')


class UserSignUpView(CreateView):
    model = User
    form_class = CustomUserForm
    template_name = 'users/signup.html'

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
    # print(drivers[0].aa.__dict__)
    driver_filter = DriverFilter(request.GET, queryset=drivers)
    

    try:
        name = request.GET['DriverSearch']
    except:
        name = {"DriverSearch":[]}

    if name:
        drivers = driver_filter.qs.filter(user__name__contains=F"{name}")
    else:
        drivers = driver_filter.qs

    if not drivers.exists():
        
        # print(request.GET.__dict__)     
        drivers = Driver.objects.all().prefetch_related("aa")
        # print(drivers)

    #TODO There can be used __range
    
    context = {'drivers':drivers, 'driver_filter': driver_filter}


    return render(request, 'users/driver_list.html', context)



def guide_list(request):
    guides = Guide.objects.all()


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


    return render(request, 'users/guide_list.html', context)  

def agent_list(request):
    agents = TourAgents.objects.all()


    agent_filter = TourAgentsFilter(request.GET, queryset=agents)
    

    def func_valid_input(key):
        try:
            name = request.GET[key]
        except:
            name = False
        return name

    name = func_valid_input('AgentSearch')
    price_start = func_valid_input('PriceStart')    
    price_to = func_valid_input('PriceTo')    
    date_start = func_valid_input('DateStart')   
    date_end = func_valid_input('DateEnd')   
    quantity = func_valid_input('Quantity')

    agents = agent_filter.qs

# #########_______________ FIlter Name________________ #############
#     if name:
#         agents = agent_filter.qs.filter(user__name__contains=F"{name}",)

#     # print(1,date_start,date_end)

# #########_______________ FIlter Date range________________ #############

#     if date_start and date_end:
#         print(2,date_start,date_end)
#     #     print(1,date_start,date_end)
#         agents = agent_filter.qs.filter(date_of_tour__range=(date_start,date_end),)

#     elif date_start and not date_end:
#         date_end = "2100-01-01"
#         print(3,date_start,date_end)
#         agents = agent_filter.qs.filter(date_of_tour__range=(date_start,date_end),) 
#     elif not date_start and date_end:
#         date_start = str(datetime.date.today())
#         print(date_start)
#         agents = agent_filter.qs.filter(date_of_tour__range=(date_start,date_end),)


# #########_______________ FIlter price range________________ #############

#     if price_start and price_to:
#         print(2,price_start,price_to)
#     #     print(1,price_start,price_to)
#         agents = agents.filter(first_to_ten_price__range=(price_start,price_to),)

#     elif price_start and not price_to:
#         price_to = 10000000000
#         print(3,price_start,price_to)
#         agents = agents.filter(first_to_ten_price__range=(price_start,price_to),) 
#     elif not price_start and price_to:
#         price_start = 0
#         agents = agents.filter(first_to_ten_price__range=(price_start,price_to),)

# #########_______________ FIlter quantity ________________ #############
#     if quantity:
#         quantity = int(quantity)
#         agents = agent_filter.qs.filter(quantity=quantity,)
        

    # if not agents.exists(): 
    #     # print(request.GET.__dict__)     
    #     agents = TourAgents.objects.all()



    context = {'agents':agents, 'agent_filter': agent_filter} 

    return render(request, 'users/agents_list.html', context)  

def login_0(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            template_dict = {'1': '/tour_agent_page', '2': '/client_page',
                            '3': '/client_page', '4': '/tour_agent_page'
                            }
            # print(form.cleaned_data['username'])
            # print(form.cleaned_data['password'])
            key = form.cleaned_data['user_choices'] 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            ####_______here must be checked if such kind of user exists_____#######
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                template_0 = template_dict[key]
                return redirect(template_0)
            else:
                return HttpResponse("wrong login")
    else:
        form = LoginForm()

    return render(request,'users/login.html', {'form':form} )

def login_1(request,key):
    # print(key)
    # print(request.GET.__dict__)
    # print(request.POST.__dict__)
    # template_dict = {'1': '/client_page', '2': '/client_page', '3': '/client_page', '4': '/tour_agent_page'}


    return redirect('/client_page')

def u_logout(request):
    logout(request)
    return redirect('/client_page')


def driver_search(request):

    if request.method == 'POST':
        print(request__dict__)

    return render(request, 'users/driver_search.html')     

def tour_list(request):

    tours = Tour.objects.all()


    tour_filter = TourFilter(request.GET, queryset=tours)
    

    def func_valid_input(key):
        try:
            name = request.GET[key]
        except:
            name = False
        return name

    name = func_valid_input('AgentSearch')
    price_start = func_valid_input('PriceStart')    
    price_to = func_valid_input('PriceTo')    
    date_start = func_valid_input('DateStart')   
    date_end = func_valid_input('DateEnd')   
    quantity = func_valid_input('Quantity')

    tours = tour_filter.qs

#########_______________ FIlter Name________________ #############
    if name:
        tours = tour_filter.qs.filter(user__name__contains=F"{name}",)

    # print(1,date_start,date_end)

#########_______________ FIlter Date range________________ #############

    if date_start and date_end:
        print(2,date_start,date_end)
    #     print(1,date_start,date_end)
        tours = tour_filter.qs.filter(date_of_tour__range=(date_start,date_end),)

    elif date_start and not date_end:
        date_end = "2100-01-01"
        print(3,date_start,date_end)
        tours = tour_filter.qs.filter(date_of_tour__range=(date_start,date_end),) 
    elif not date_start and date_end:
        date_start = str(datetime.date.today())
        print(date_start)
        tours = tour_filter.qs.filter(date_of_tour__range=(date_start,date_end),)


#########_______________ FIlter price range________________ #############

    if price_start and price_to:
        print(2,price_start,price_to)
    #     print(1,price_start,price_to)
        tours = tours.filter(first_to_ten_price__range=(price_start,price_to),)

    elif price_start and not price_to:
        price_to = 10000000000
        print(3,price_start,price_to)
        tours = tours.filter(first_to_ten_price__range=(price_start,price_to),) 
    elif not price_start and price_to:
        price_start = 0
        tours = tours.filter(first_to_ten_price__range=(price_start,price_to),)

#########_______________ FIlter quantity ________________ #############
    if quantity:
        quantity = int(quantity)
        tours = tour_filter.qs.filter(quantity=quantity,)
        

    # if not agents.exists(): 
    #     # print(request.GET.__dict__)     
    #     agents = TourAgents.objects.all()

    context = {'tours':tours, 'tour_filter': tour_filter} 

    return render(request, 'users/tour_list.html', context)  

def tour_agent_page(request):
    if request.method == "POST":
        form = TourCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('tour_agent_page')
    else:
        form = TourCreationForm()

    return render(request, 'users/tour_agent_page.html', {"form": form})
