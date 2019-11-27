from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.db import transaction

from django.contrib.sites.models import Site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import request
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import update_session_auth_hash
from users.tokens import account_activation_token

from users.models import *
from users.forms import *


# Create your views here.
@login_required(login_url="/users/")
@permission_required('users.add_user', raise_exception=True)
@transaction.atomic
def add_user_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        details_form = UserDetailsForm(request.POST)
        if user_form.is_valid() and details_form.is_valid():
            user = user_form.save()
            user.profile.bio = details_form.cleaned_data.get('bio')
            group = details_form.cleaned_data.get('group')
            department = details_form.cleaned_data.get('department')
            user.profile.group.add(group[0].pk)
            dept = Department.objects.get(pk=department.pk)
            user.profile.department = dept
            user.profile.role = details_form.cleaned_data.get('role')
            user.profile.save()

            # Email sending functionality
            subject = "Activate Your Ratable Account"
            current_site = Site.objects.get_current()
            sender = "atst.acc19@gmail.com"

            # passing in the context vairables
            text_content = render_to_string(
                "registration/emails/account_activation_email.txt",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            html_content = render_to_string(
                "registration/emails/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )

            msg = EmailMultiAlternatives(
                subject, text_content, sender, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("account_activation_sent")
        else:
            return redirect('profile')
            # user_form = UserForm()
            # return render(request, 'registration/add_user.html', {'user_form': user_form, 'details_form': details_form})
    else:
        user_form = UserForm()
        details_form = UserDetailsForm()
    return render(request, 'registration/add_user.html', {
        'user_form': user_form,
        'details_form': details_form
    })


def account_activation_sent(request):
    return render(request, 'registration/emails/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        subject = "Welcome to Ratable"
        sender = "atst.acc19@gmail.com"

        # passing in the context vairables
        text_content = render_to_string(
            "registration/emails/welcome_email.txt", {"user": user})
        html_content = render_to_string(
            "registration/emails/welcome_email.html", {"user": user})

        msg = EmailMultiAlternatives(
            subject, text_content, sender, [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return redirect("reset")
    else:
        return render(request, "registration/emails/account_activation_invalid.html")


def login_user(request):
    # logout(request)
    next_page = ''
    username = password = ''
    if 'next' in request.POST:
        next_page = request.POST['next']
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next_page:
                    return redirect(next_page)
                return redirect('landing_page')
    return render(request, 'registration/login.html')


def set_password_view(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    form = UserSetPasswordForm(request.POST, instance=user)
    print(form.data)
    print(form.fields)
    if request.method == "POST":

        if form.is_valid():
            print("valid")
            password = form.cleaned_data['password2']
            form.save()
            return redirect("edit_profile")

    return render(request, 'registration/password_set_form.html', {'user': user, 'form': form})


@login_required(login_url="/users/")
def profile(request):

    current_user = request.user
    user_data = User.objects.get(id=current_user.id)
    user_profile = UserProfile.objects.get(id=current_user.id)

    return render(
        request,
        "registration/profile.html",
        {"user_data": user_data, "user_profile": user_profile},
    )


@login_required(login_url="/users/")  # only logged in users should access this
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
            {"noodle": user.id, "noodle_form": user_form,
                "formset": formset, "user": user},
        )
    else:
        raise PermissionDenied


@login_required(login_url="/users/")
def group_create_view(request):
    perms = Permission.objects.all()
    form = CustomGroupForm(request.POST)
    if form.is_valid():
        grp = form.cleaned_data['name']
        group, created = Group.objects.get_or_create(name=grp)
        if created:
            group.permissions.set(form.cleaned_data['permissions'])
        form = CustomGroupForm()
    context = {
        'form': form,
        'perms': perms,
    }
    return render(request, "groups/group_create.html", context)


@login_required(login_url="/users/")
def group_list_view(request):
    queryset = CustomGroup.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "groups/group_list.html", context)


@login_required(login_url="/users/")
def group_delete_view(request):
    pass
