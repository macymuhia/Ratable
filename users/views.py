from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *

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


@login_required(login_url="")  # only logged in users should access this
def edit_profile(request):

    current_user = request.user
    user = User.objects.get(id=current_user.id)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserProfileForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(
        User, UserProfile, fields=("photo", "phone", "bio")
    )
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(
                request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(
                request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(
                    request.POST, request.FILES, instance=created_user
                )

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return redirect("profile")

        return render(
            request,
            "registration/edit_profile.html",
            {"noodle": user.id, "noodle_form": user_form, "formset": formset},
        )
    else:
        raise PermissionDenied


@login_required(login_url="")
def add_user(request):
    form = AddUserForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = AddUserForm()

    return render(request, "add_user.html", {"form": form})
