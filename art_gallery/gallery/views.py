from .forms import *
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
import json
import datetime
from django.urls import reverse_lazy, reverse
from .models import Artists, Painting, Gallery, Profile
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user

@login_required
@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def painting(request):
    painting = Painting.objects.all()
    #print(painting)
    p1 = Painting.objects.get(id=3)
    #print(p1)
    #print(p1.total_likes())
    likes = []
    
    for i in painting:
        p1 = Painting.objects.get(id=i.id)
        p1.total_likes = p1.total_likes()
        

    context = {'painting':painting,}
    #print(context)
    return render(request, 'gallery/painting.html', context)


@allowed_users(allowed_roles=['admin','artist']) 
def addpainting(request):
    context = {}
    if request.method == "POST":
        
        form = PaintingForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Painting()
            
            post.p_type = form.cleaned_data.get("p_type")
            post.title = form.cleaned_data.get("title")
            post.artist = form.cleaned_data.get("artist")
            post.yearmade = form.cleaned_data.get("yearmade")
            post.price = form.cleaned_data.get("price")
            post.sold = form.cleaned_data.get("sold")
            post.image = form.cleaned_data.get("image")
            
            post.save()
            context['form']= form
            return render( request, "gallery/success.html", context)
        
    else:
        form = PaintingForm()
        context['form']= form
        return render( request, "gallery/addpainting.html", context)

@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def cart(request):
	context = {}
	return render(request, 'gallery/cart.html', context)

@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def booking(request):
	context = {}
	return render(request, 'gallery/booking.html', context)

@login_required
@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def profile(request):
    user = request.user
    #print(user)
    profile = Profile.objects.get(username=user)
    print(profile)
    context = {'profile':profile}
    
    return render(request, 'gallery/profile.html', context)

@login_required
@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def gallery(request):
    gallery = Gallery.objects.all()
    context = {'gallery': gallery}
    return render(request, 'gallery/gallery.html', context)

@allowed_users(allowed_roles=['admin','artist']) 
def addgallery(request):
    context = {}
    if request.method == "POST":
        
        form = GalleryForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Gallery()
            
            post.artist = form.cleaned_data.get("artist")
            post.g_name = form.cleaned_data.get("g_name")
            post.location = form.cleaned_data.get("location")
            post.image = form.cleaned_data.get("image")
            
            post.save()
            context['form']= form
            return render( request, "gallery/success.html", context)
        
    else:
        form = GalleryForm()
        context['form']= form
        return render( request, "gallery/addgallery.html", context)

@login_required
@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def artist_info(request, pk):
    artist = Artists.objects.get(id=pk)

    print(artist)
    galleries = []
    
    g = Gallery.objects.filter(artist=artist)
    print(g)
    paintings = []
    p = Painting.objects.filter(artist=artist)
    print(p)

    context = {'artist':artist, 'gallery':g, 'painting':p}


    return render(request, "gallery/artist_info.html", context)

@allowed_users(allowed_roles=['admin','artist', 'customer'])    
def viewartist(request):
    #Store.objects.in_bulk([1])
    #gallery = Gallery.objects.exclude(3)
    gallery1 = Gallery.objects.get(id=1)
    gallery2 = Gallery.objects.get(id=2)
    
    artist1 = Artists.objects.get(id=1)
    artist2 = Artists.objects.get(id=2)

    painting1 = Painting.objects.get(id=1)
    painting2 = Painting.objects.get(id=2)

    context = {'gallery': (gallery1,gallery2), 'artist': (artist1, artist2), 'painting': (painting1, painting2)}
    return render(request, "gallery/viewartist.html", context)

@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def dashboard(request):
    context = {}
    return render(request, 'gallery/dashboard.html', context)

@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def event(request):
    context = {}
    return render(request, 'gallery/event.html', context)

@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def exhibition(request):
    exhibitions = Exhibitions.objects.all()
    context = {'exhibitions':exhibitions}
    return render(request, 'gallery/exhibition.html', context)

@allowed_users(allowed_roles=['admin','artist']) 
def addexhibition(request): 
    context = {} 
    if request.method == "POST": 
        form = ExhibitionForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Exhibitions()
            
            post.gallary = form.cleaned_data.get("gallary")
            post.exb_type = form.cleaned_data.get("exb_type")
            post.exb_name = form.cleaned_data.get("exb_name")
            post.start_date = form.cleaned_data.get("start_date")
            post.end_date = form.cleaned_data.get("end_date")
            post.s_time = form.cleaned_data.get("s_time")
            post.end_time = form.cleaned_data.get("end_time")
            post.image = form.cleaned_data.get("image")
            
            post.save() 
            context['form']= form 
            return render(request, "gallery/success.html", context) 
            
    else: 
        form = ExhibitionForm() 
        context['form']= form  
        return render(request, "gallery/addexhibition.html", context) 

@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def list_of_events(request):
    list_of_events = Events.objects.all()
    context = {'list_of_events':list_of_events}
    return render(request, 'gallery/list_of_events.html', context)

@allowed_users(allowed_roles=['admin','artist']) 
def addevent(request): 
    context = {} 
    if request.method == "POST": 
        form = EventForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Events()
            
            post.exhibition = form.cleaned_data.get("exhibition")
            post.e_name = form.cleaned_data.get("e_name")
            post.date = form.cleaned_data.get("date")
            post.s_time = form.cleaned_data.get("s_time")
            post.end_time = form.cleaned_data.get("end_time")
            
            post.save() 
            context['form']= form 
            return render( request, "gallery/success.html", context) 
            
    else: 
        form = EventForm() 
        context['form']= form  
        return render( request, "gallery/addevent.html", context) 

@allowed_users(allowed_roles=['admin','artist', 'customer']) 
def artist(request):
    artist = Artists.objects.all()
    
    #print(artist[1])
    galleries = [[0]*len(artist)]*len(artist)
    
    for i in range(len(artist)):
        l = Gallery.objects.filter(artist=artist[i])
        galleries[i] = l
    
    #print(galleries)
    
    context = {'artist':artist, 'gallery':galleries}
    return render(request, 'gallery/artist.html', context)

#ONLY ALLOWED TO ADMIN
@allowed_users(allowed_roles=['admin']) 
def addartist(request): 
    context = {} 
    if request.method == "POST": 
        form = ArtistForm(request.POST, request.FILES)
        #print(form)
        i = 3
        if form.is_valid():
            post = Artists()
            
            post.a_name = form.cleaned_data.get("a_name")
            post.email = form.cleaned_data.get("email")
            post.address = form.cleaned_data.get("address")
            post.phone = form.cleaned_data.get("phone")
            post.age = form.cleaned_data.get("age")
            post.style = form.cleaned_data.get("style")
            post.image = form.cleaned_data.get("image") 
            post.save() 
            context['form']= form 
            return render( request, "gallery/success.html", context) 
            
    else: 
        form = ArtistForm() 
        context['form']= form  
        return render( request, "gallery/addartist.html", context) 


def gallery_exhib(request, pk):
    gallery = Gallery.objects.get(id=pk)
    #print(gallery)
    exhibition = []
    e = Exhibitions.objects.filter(gallary=gallery)
    #print(e)
    
    context = {'gallery':gallery, 'exhibition':e}
    return render(request, "gallery/gallery_exhib.html", context)

def exhib_event(request, pk):
    exhibition = Exhibitions.objects.get(id=pk)
    #print(exhibition)
    events = []
    e = Events.objects.filter(exhibition=exhibition)
    #print(e)
    
    context = {'exhibition':exhibition, 'events':e}
    return render(request, "gallery/exhib_event.html", context)

def like(request, pk):
    painting = get_object_or_404(Painting, id=request.POST.get('painting_id'))
    painting.likes.add(request.user)
    return HttpResponseRedirect(reverse('painting'))
