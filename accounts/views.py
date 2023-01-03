from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterUserForm, ShippingForm
from django.contrib import messages, auth
from .models import User, UserProfile
from django.contrib.auth.decorators import login_required
from orders.models import *
 
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
    try:
        for key in list(request.session.keys()):
            if key == 'session-catch': 
                continue
            else:
                del request.session[key]
    except KeyError:
        pass
    
    return redirect('home')

@login_required(login_url='login')
def settings(request):
    return render(request, 'accounts/settings.html')

@login_required(login_url='login')
def ordersHistory(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    context = {'orders': orders}
    return render(request, 'accounts/ordersHistory.html', context)
    
@login_required(login_url='login')
def orderDetail(request, id):
    order = Order.objects.get(pk=id)
    orderdetail = OrderProduct.objects.filter(order=order).order_by('-id')
    context = {'orderdetail': orderdetail}
    return render(request, 'accounts/orderDetail.html', context)
        

@login_required(login_url='login')
def shippingAddress(request):    
    try:
        address = ShippingAddress.objects.get(user=request.user.id)
    except ShippingAddress.DoesNotExist:
        address = None
        
    form = ShippingForm(instance=address)
    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=address)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()

            return redirect('profile')

    context = {'form':form}

    return render(request, 'accounts/shippingAddress.html', context)
    
    # profile = get_object_or_404(UserProfile, user=request.user)   
    
    # if request.method == 'POST':
    #     profile_form = UserProfileForm(request.POST, instance=profile)
    #     if profile_form.is_valid():
    #         profile_form.save()
    #         return redirect('profile')
    #     else:
    #         print(profile_form.errors)
    # else:  
    #     profile_form = UserProfileForm(instance = profile)
    
    # context = {
    #     'profile_form': profile_form,
    #     'profile': profile,
    # }
    # return render(request, 'accounts/shippingAddress.html', context)

@login_required(login_url='login')
def deleteAccount(request):
    user = User.objects.get(id=request.user.id) 
    
    if request.method == 'POST':
        user.delete()
        messages.info(request, 'Account has been deleted.')
        return redirect ('home')
    return render (request, 'accounts/delete.html')