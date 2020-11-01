from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('cart/', views.cart, name = "cart"),
    path('profile/', views.profile, name = "profile"),
    path('painting/', views.painting, name = "painting"),
    path('event/', views.event, name = "event"),
    path('addevent/', views.addevent, name = "addevent"),
    path('list_of_events/', views.list_of_events, name = "list_of_events"),
    path('exhibition/', views.exhibition, name = "exhibition"),
    path('exhib_event/<str:pk>', views.exhib_event, name = "exhib_event"),
    path('addexhibition/', views.addexhibition, name = "addexhibition"),
    path('artist/', views.artist, name = "artist"),
    path('artist_info/<str:pk>', views.artist_info, name = "artist_info"),
    path('addartist/', views.addartist, name = "addartist"),
    path('addpainting/', views.addpainting, name = "addpainting"),
    path('viewartist/', views.viewartist, name = "viewartist"),
    path('gallery/', views.gallery, name = "gallery"),
    path('gallery_exhib/<str:pk>', views.gallery_exhib, name = "gallery_exhib"),
    path('addgallery/', views.addgallery, name = "addgallery"),
    path('booking/', views.booking, name = "booking"),
    path('like/<int:pk>', views.like, name = "like_painting"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)