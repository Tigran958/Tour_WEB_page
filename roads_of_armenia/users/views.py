from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse

from .forms import * 
from .models import User, Driver, CarImageModel, Guide, TourAgents, Tour, TourImage

from .filters import DriverFilter, TourAgentsFilter, GuideFilter, TourFilter
import datetime


def func_valid_input(key):
    try:
        name = request.GET[key]
    except:
        name = False
    return name



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
        ###__________function for formset choice________###
        def filter_type(TitleFormSet,key):  
            data = super(UserSignUpView, self).get_context_data(**kwargs)
            if self.request.POST:
                print(self.request.FILES)
                data['titles'] = TitleFormSet(self.request.POST,self.request.FILES)
                
            else:
                data['titles'] = TitleFormSet()
                data['form'].fields['user_choices'].initial = key
            return data    

        data = filter_type(user_coll_type,filter_key)
        
        return data

    def form_valid(self, form):
        
        context = self.get_context_data()
        titles = context["titles"]
        # print(titles.__dict__)

        self.object = form.save()
        user_choices = form.cleaned_data.get('user_choices')

        if titles.is_valid(): 
            titles.instance = self.object
            titles.save()
            valid = super().form_valid(form)
            self.username = form.cleaned_data['email']
            self.password = form.cleaned_data['password1']
            self.user_choices = form.cleaned_data.get('user_choices')
            ####_______here must be checked if such kind of user exists_____#######
            self.user = authenticate(email=self.username,password=self.password)
        
            if self.user is not None:
                login(self.request,self.user)

        return valid
    # @login_required    
    def get_success_url(self,**kwargs):
        url_dict = {'1': '/driver_list', '2': '/client_page',
                            '3': '/guide_list', '4': '/tour_creation'
                            }
        url = url_dict[str(self.kwargs['key'])]
        # print(self.user.is_authenticated)
        return url

def client_page(request):
    return render(request, 'users/client_page.html')

def tour_creation(request):
    if request.user.is_authenticated:
        agent = TourAgents.objects.get(user__id=request.user.id) 
        tour = Tour.objects.all().filter(tour__id=agent.id)
        context = {'tour':tour}
    # else:
    #     tour = Tour.objects.all()
    #     context = {'tour':tour}
    return render(request, 'users/tour_agent.html', context)

# @login_required
def driver_list(request):

    def func_valid_input(key):
        try:
            name = request.POST[key]
        except:
            name = False
        return name
    drivers = Driver.objects.all().prefetch_related("aa")

    driver_filter = DriverFilter(request.POST, queryset=drivers)
    

    name = func_valid_input('DriverSearch')

    if name:
        drivers = drivers.filter(name__contains=F"{name}")
    # else:
    #     drivers = driver_filter.qs

    # if not drivers.exists():
        
            
    #     drivers = Driver.objects.all().prefetch_related("aa")

    context = {'drivers':drivers, 'driver_filter': driver_filter}


    return render(request, 'users/driver_list.html', context)

    # else:
    #     return redirect("in/")    
    
    


def guide_list(request):

    def func_valid_input(key):
        try:
            name = request.POST[key]
        except:
            name = False
        return name

    guides = Guide.objects.all()


    guide_filter = GuideFilter(request.POST, queryset=guides)
    
    guides = guide_filter.qs

    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            name = form.cleaned_data['name']
    else:
        form = GuideForm() 

    try:
        type(language)
    except:
        language = False
    try:
        type(name)
    except:
        name = False


    if name:
        guides = guides.filter(name__contains=F"{name}") #պետք ա անունը փոխել գիդինը
    if language:
        guides = guides.filter(language__contains=language)
        

    # if not guides.exists():
    #     guides = Guide.objects.all()
    

    context = {'guides':guides, 'guide_filter':guide_filter, 'form':form}


    return render(request, 'users/guide_list.html', context)  

def agent_list(request):
    agents = TourAgents.objects.all()


    agent_filter = TourAgentsFilter(request.GET, queryset=agents)
    

    name = func_valid_input('AgentSearch')

    agents = agent_filter.qs


    context = {'agents':agents, 'agent_filter': agent_filter} 

    return render(request, 'users/agents_list.html', context)  



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


    #########_______________ FIlter Date range________________ #############

    if date_start and date_end:
        tours = tour_filter.qs.filter(date_of_tour__range=(date_start,date_end),)

    elif date_start and not date_end:
        date_end = "2100-01-01"
        tours = tour_filter.qs.filter(date_of_tour__range=(date_start,date_end),) 
    elif not date_start and date_end:
        date_start = str(datetime.date.today())
        print(date_start)
        tours = tour_filter.qs.filter(date_of_tour__range=(date_start,date_end),)


    #########_______________ FIlter price range________________ #############

    if price_start and price_to:
        tours = tours.filter(first_to_ten_price__range=(price_start,price_to),)

    elif price_start and not price_to:
        price_to = 10000000000
        tours = tours.filter(first_to_ten_price__range=(price_start,price_to),) 
    elif not price_start and price_to:
        price_start = 0
        tours = tours.filter(first_to_ten_price__range=(price_start,price_to),)

    #########_______________ FIlter quantity ________________ #############
    if quantity:
        quantity = int(quantity)
        tours = tour_filter.qs.filter(quantity=quantity,)
        


    context = {'tours':tours, 'tour_filter': tour_filter} 

    return render(request, 'users/tour_list.html', context)  


@login_required
def pic_upload(request,user_id=1):
    if request.method == "POST":

        form = TourCreationForm(request.POST)
        if form.is_valid():
            form.save()
            tour_agent = TourAgents.objects.get(user_id=user_id)
            tour_obj = Tour.objects.all().filter(tour_id=tour_agent.id)
            image = tour_obj.last()
            
            for afile in request.FILES.getlist('files'):
                tourimage = TourImage.objects.create(image=image,mainimage=afile)
            return redirect('tour_creation') 
    else:
        form = TourCreationForm()
        form.initial['tour'] = TourAgents.objects.get(user_id=user_id)
        
    return render(request, 'users/tour_creation.html', {"form": form})

def login_0(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            template_dict = {'1': '/driver_list', '2': '/client_page',
                            '3': '/guide_list', '4': '/tour_creation'
                            }
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)

            if user is not None:
                
                login(request,user)
                template_0 = template_dict[str(user.user_choices)]
                return redirect(template_0)
            else:
                print(request.POST)
                return HttpResponse("wrong login")
    else:
        
        form = LoginForm()

    return render(request,'users/login.html', {'form':form} )


def u_logout(request):
    logout(request)
    return redirect('/client_page')

