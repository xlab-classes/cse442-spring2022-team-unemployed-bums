from django.urls import path
from profilepage.views import Index

urlpatterns = [
    path('', Index.as_view(), name='profile_index')
]