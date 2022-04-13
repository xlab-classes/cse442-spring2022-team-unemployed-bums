from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', profile, name="profile-page"),
    path('editprofile/', editProfile, name="edit-bio-interests"),

    path('image_upload/', editProfilePic, name="image_upload"),
    path('success', success, name = 'success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)