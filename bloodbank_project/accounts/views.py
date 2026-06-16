from django.shortcuts import render



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm , ProfileEditForm ,ChangePasswordForm
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

            login(request, user)

            messages.success(request, f'Welcome to Blood Bank, {first_name}!')
            return redirect_after_login(user)

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

@login_required(login_url='accounts:login')
def profile_view(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='accounts:login')
def edit_profile_view(request):
    user = request.user
    
    if request.method == 'GET':
        form = ProfileEditForm(
            user=user,
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'blood_type': user.blood_type,
                'age': user.age,
                'address': user.address,
            }
        )
        return render(request, 'accounts/edit_profile.html', {'form': form})
    
    if request.method == 'POST':
        form = ProfileEditForm(user=user, data=request.POST)
        
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.blood_type = form.cleaned_data['blood_type']
            user.age = form.cleaned_data['age']
            user.address = form.cleaned_data['address']
            user.save()
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
        
        return render(request, 'accounts/edit_profile.html', {'form': form})
    
@login_required(login_url='accounts:login')
def add_role_view(request, role):
    user = request.user
    
    if role == 'donor':
        if user.is_donor:
            messages.warning(request, 'You are already registered as a donor.')
        else:
            user.is_donor = True
            user.save()
            messages.success(request, 'You are now registered as a donor! You can now donate blood.')
    
    elif role == 'receiver':
        if user.is_receiver:
            messages.warning(request, 'You are already registered as a receiver.')
        else:
            user.is_receiver = True
            user.save()
            messages.success(request, 'You are now registered as a receiver! You can now request blood.')
    
    elif role == 'hospital':
        # Block hospital self-registration
        messages.error(request, 'Hospital registration requires admin approval. Please contact admin.')
    
    else:
        messages.error(request, 'Invalid role.')
    
    return redirect('accounts:profile')

@login_required(login_url='accounts:login')
def change_password_view(request):
    user = request.user
    
    if request.method == 'GET':
        form = ChangePasswordForm(user=user)
        return render(request, 'accounts/change_password.html', {'form': form})
    
    if request.method == 'POST':
        form = ChangePasswordForm(user=user, data=request.POST)
        
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            
            # Re-login the user after password change
            # (changing password invalidates the session)
            login(request, user)
            
            messages.success(request, 'Password changed successfully!')
            return redirect('accounts:profile')
        
        return render(request, 'accounts/change_password.html', {'form': form})