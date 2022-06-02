from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('users:profile'))

    return render(request, 'users/login.html')


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('users:profile'))

    return render(request, 'users/register.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect(reverse('homepage'))


@login_required
def profile_view(request):
    # if request.user.is_authenticated:
    #     return HttpResponse('This is the profile route.')
    #
    # return redirect(reverse('users:login'))

    return HttpResponse('This is the profile route.')
