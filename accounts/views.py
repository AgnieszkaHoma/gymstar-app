from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterUserForm, UserProfileForm
from django.contrib import messages, auth
from .models import User, UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('profile')
    elif request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()    
            messages.success(request, 'Registration successful! Log in.')     
            return redirect('register')
        
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = RegisterUserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

@login_required(login_url='login')
def profile(request):
    
    profile = UserProfile.objects.get(user_id=request.user.id)
    context = {
        'profile': profile,
    }
    return render(request, 'accounts/profile.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, try again.')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='login')
def settings(request):
    return render(request, 'accounts/settings.html')

@login_required(login_url='login')
def ordersHistory(request):
    return render(request, 'accounts/ordersHistory.html')

@login_required(login_url='login')
def myDetails(request):
    profile = get_object_or_404(UserProfile, user=request.user)   
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
        else:
            print(profile_form.errors)
    else:  
        profile_form = UserProfileForm(instance = profile)
    
    context = {
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request, 'accounts/myDetails.html', context)