from django.urls import path
from .views import profile, editProfile

urlpatterns = [
    path('', profile, name="profile-page"),
    #path('editprofile/', editProfile, name="edit-bio-interests")
    path('editprofile/', editProfile, name="edit-bio-interests")
]