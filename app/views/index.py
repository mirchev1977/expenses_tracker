from django.shortcuts import render

from app.forms.profiles import ProfileForm
from app.models import Profile
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        pass
    else:
        return create_profile(request);