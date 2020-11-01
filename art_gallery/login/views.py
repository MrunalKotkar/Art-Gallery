from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from gallery.models import *
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
# Create your views here.   


def register(request):
    
    if request.method == "POST":
        #import pdb;pdb.set_trace()
        form = UserRegisterForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        c_form = CustomerForm(request.POST)

        if form.is_valid():
            user = form.save()
            p_form.save()
            c_form.save()
            username = form.cleaned_data.get('username')
            print(username)

            #Default Group of User -> Customer
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, f'Account created for {username}!')
            return redirect('/login')
        else:
            print(form.errors)


    else:
        form =  UserRegisterForm()
        #p_form = ProfileUpdateForm(request.POST)
        #c_form = CustomerForm(request.POST)
    return render(request, 'login/register.html', {'form':form})


def index(request):
    gallery1 = Gallery.objects.get(id=8)
    gallery2 = Gallery.objects.get(id=9)
    gallery3 = Gallery.objects.get(id=10)
    artist1 = Artists.objects.get(id=9)
    artist2 = Artists.objects.get(id=10)
    artist3 = Artists.objects.get(id=11)
    painting1 = Painting.objects.get(id=3)
    painting2 = Painting.objects.get(id=4)
    painting3 = Painting.objects.get(id=5)

    context = {'gallery': (gallery1,gallery2,gallery3), 'artist': (artist1, artist2,artist3), 'painting': (painting1, painting2,painting3)}
    
    return render(request, 'login/index.html', context)






