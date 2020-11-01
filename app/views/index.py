from django.shortcuts import render

from app.models import Profile


def index(request):
    if Profile.objects.exists():
        pass
    else:
        return render(request, 'home-no-profile.html')