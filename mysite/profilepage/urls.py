from django.urls import path
from profilepage.views import Index
from . import views

urlpatterns = [
    path('', Index.as_view(), name='profile_index'),
    path('add_follower', views.add_follower, name='add_follower'),
    path('remove_follower', views.remove_follower, name='remove_follower'),
    path('delete_account', views.deleteAccount, name='delete_account'),
]