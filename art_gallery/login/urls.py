from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as v
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name = "index"),
    path('login/', v.LoginView.as_view(), name = "login"),
    path('register/', views.register, name = "register"),
    path('password-reset/', v.PasswordResetView.as_view(template_name='login/password_reset.html'), name='password_reset'),
    path('password-reset_done/', v.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', v.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),  
    path('password-reset-complete/', v.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete'), 
]

