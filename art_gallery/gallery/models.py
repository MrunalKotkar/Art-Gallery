from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Artists(models.Model):
    a_name=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    age=models.IntegerField()
    style=models.CharField(max_length=30)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.a_name

class Painting(models.Model):
    artist = models.ForeignKey(Artists, null=True, on_delete= models.SET_NULL)
    p_type=models.CharField(max_length=40)
    title=models.CharField(max_length=30)
    yearmade=models.IntegerField()
    price=models.IntegerField()
    sold=models.CharField(max_length=30)
    image=models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="paintings")
    tot_likes = models.IntegerField(null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    artist = models.ForeignKey(Artists, null=True, on_delete= models.SET_NULL)
    g_name = models.CharField(max_length=200, null= True)
    location = models.CharField(max_length=300)
    image = models.ImageField(null= True, blank = True)

    def __str__(self):
        return self.g_name


class Profile(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return str(self.username)


class Exhibitions(models.Model):
    gallary = models.ForeignKey(Gallery, null = True, on_delete = models.SET_NULL)
    exb_type = models.CharField(max_length=50)
    exb_name = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank = True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank = True, null=True)
    s_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank= True,null=True)
    image = models.ImageField(null= True, blank = True)

    def __str__(self):
        return self.exb_name


class Events(models.Model):
    exhibition = models.ForeignKey(Exhibitions, null = True, on_delete=models.SET_NULL)
    e_name = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False, blank = True, null=True)
    s_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)

    def __str__(self):
        return self.e_name

class Customer(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.user


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    painting = models.ForeignKey(Painting, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
