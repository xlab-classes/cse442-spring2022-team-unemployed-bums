from django.urls import path
from profilepage.views import Index
from profilepage.views import Idk
from . import views

urlpatterns = [
    path('', Index.as_view(), name='profile_index'),
    #path('settings/', Index.profileSettings(GET), name='form_page')
    path('settings/',Idk.as_view(), name='edit_profile')
]