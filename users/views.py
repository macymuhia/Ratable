from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.
@login_required(login_url="")
def profile(request):

    current_user = request.user
    user_data = User.objects.get(id=current_user.id)
    user_profile = UserProfile.objects.get(id=current_user.id)

    return render(
        request,
        "registration/profile.html",
        {"user_data": user_data, "user_profile": user_profile},
    )
