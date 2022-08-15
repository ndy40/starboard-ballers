from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, RegisterForm

# Create your views here.


@require_http_methods(['GET', 'POST'])
def login_user(request):
    form = LoginForm(request.POST or None)
    context = {}

    if request.method == 'POST' and form.is_valid():
        user = authenticate(request, username=form.cleaned_data['username'], password='randompassword')

        if user:
            login(request, user)
            return redirect('sessions')
        else:
            messages.error(request, message="failed login")

    context['form'] = form

    return render(request, 'frontend/login.html', context=context)


@require_http_methods(['GET'])
def logout_user(request):
    logout(request)
    return redirect('login')


@require_http_methods(['GET', 'POST'])
def register(request):
    form = RegisterForm(request.POST or None)
    context = {}

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('sessions')

    context['form'] = form

    return render(request, 'frontend/register.html', context=context)
