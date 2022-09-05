from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


def start(request):
    return render(request, template_name='news/main.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, template_name='news/register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, template_name='news/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            mail = send_mail('subject', form.cleaned_data['content'], 'vahlovaleksandar@yandex.ru', [
                # 'vakhlov.av@phystech.edu',
                # 'vahlovaleksandar@yandex.ru',
                'parol.neznau22@gmail.com',
            ], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправления')

    else:
        form = ContactForm()
    return render(request, template_name='news/mail.html', context={'form': form})
