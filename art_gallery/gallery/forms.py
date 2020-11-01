from django import forms 
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArtistForm(ModelForm): 
    class Meta:
        model = Artists
        fields = '__all__'
    
class PaintingForm(ModelForm):
    class Meta:
        model = Painting
        exclude = ['likes', 'tot_likes']

class GalleryForm(ModelForm): 
    class Meta:
        model = Gallery
        fields = '__all__'

class ExhibitionForm(ModelForm): 
    class Meta:
        model = Exhibitions
        fields = '__all__'

class EventForm(ModelForm): 
    class Meta:
        model = Events
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'