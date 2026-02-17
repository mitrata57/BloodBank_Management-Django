from django.shortcuts import render



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            blood_type = form.cleaned_data['blood_type']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = CustomUser.objects.create_user(
                phone_number=phone_number,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                blood_type=blood_type,
                age=age,
                address=address,
            )

            if role == 'donor':
                user.is_donor = True
            elif role == 'receiver':
                user.is_receiver = True
            elif role == 'hospital':
                user.is_hospital = True

            user.save()

            messages.success(request, f'Account created! Welcome, {first_name}. Please login.')
            return redirect('accounts:login')

        return render(request, 'accounts/register.html', {'form': form})
    


def login_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {})

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name()}!')
            return redirect_after_login(user)
        else:
            messages.error(request, 'Invalid phone/email or password.')
            return render(request, 'accounts/login.html', {})


def redirect_after_login(user):
    if user.is_superuser:
        return redirect('admin:index')
    elif user.is_donor:
        return redirect('donor:dashboard')
    elif user.is_receiver:
        return redirect('receiver:dashboard')
    elif user.is_hospital:
        return redirect('hospital:dashboard')
    else:
        return redirect('core:home')
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('core:home')