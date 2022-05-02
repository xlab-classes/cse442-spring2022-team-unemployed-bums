"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from Register import views as v 
from django.contrib.auth import views as auth_views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name = "register"), 
    path('edit_profile/', v.profile, name ="profile"),
    path('profile/', v.userprofile, name ="userprofile"),
    path('', include("main.urls")),
    path('login/', auth_views.LoginView.as_view(), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logout.html'), name = 'logout'),
    path('authenticated/', v.authenticated, name = "authenticated"),
    path('registered/', v.registered, name = "registered"),
    path('home/', include('home.urls'), name = "homepage"),
    path('listingcreation/', include('listingcreation.urls')),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('profile/add_follower', v.add_follower, name='add_follower'),
    path('profile/remove_follower', v.remove_follower, name='remove_follower'),
    path('profile/delete_account', v.delete_account, name ="delete_account"),
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
