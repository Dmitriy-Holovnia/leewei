from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, ContactForm, ProfileForm
from .services import send_confirmation_email, activate_account
from .models import Profile




class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            email = form.cleaned_data.get('email')
            send_confirmation_email(request, user, email)
            return render(request, 'information/confirm-account.html', {'name': user.username})
        return render(request, 'information/error.html', {'error': 'Ошибка при отправки сообщения'})

    else:
        form = RegisterForm
        return render(request, 'auth/register.html', {'form': form})

def activate(request, uidb64, token):
    if activate_account(request, uidb64, token):
        return render(request, 'information/success-singup.html')
    else:
        return render(request, 'information/error.html', {'error': 'Ошибка регистрации'})


def get_home(request):
    return render(request, 'trading/home.html')

def get_about(request):
    return render(request, 'trading/about.html')

def get_courses(request):
    return render(request, 'trading/courses.html')

def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return render(request, 'information/message-sent.html', {'name': name})
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'trading/contact.html', context)

def get_error(request):
    return render(request, 'information/error.html', {'error': 'Ошибка :('})

@login_required
def get_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            profile = Profile.objects.get(username=request.user.username)
            profile.first_name = first_name
            profile.last_name = last_name
            profile.save()
            return redirect('profile')
    else:
        user = request.user
        initial_dict = { 
        "email" : user.email, 
        "first_name" : user.first_name, 
        "last_name": user.last_name, 
        } 
        form = ProfileForm(initial=initial_dict)
        return render(request, 'trading/profile.html', {'form': form})

def get_test(request):
    user = request.user
    return render(request, 'test.html', {'user': user})