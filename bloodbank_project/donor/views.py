from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from accounts.decorators import donor_required
from .models import Donation
from .forms import DonationForm


@donor_required
def dashboard(request):
    user = request.user
    donations = Donation.objects.filter(donor=user)
    total_donations = donations.count()
    
   
    last_donation = donations.first()  
    if last_donation:
        next_eligible = last_donation.donated_on + timedelta(days=90)
        days_remaining = (next_eligible - timezone.now().date()).days
        if days_remaining <= 0:
            next_eligible_display = 'Eligible Now!'
        else:
            next_eligible_display = f'{next_eligible.strftime("%b %d, %Y")} ({days_remaining} days)'
    else:
        next_eligible_display = 'Eligible Now!'
    

    lives_saved = total_donations * 3
    
    context = {
        'total_donations': total_donations,
        'next_eligible': next_eligible_display,
        'lives_saved': lives_saved,
        'recent_donations': donations[:5], 
    }
    return render(request, 'donor/dashboard.html', context)


@donor_required
def record_donation(request):
    if request.method == 'GET':
        form = DonationForm()
        return render(request, 'donor/record_donation.html', {'form': form})
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        
        if form.is_valid():
            donation = Donation.objects.create(
                donor=request.user,
                blood_type=request.user.blood_type,  # auto from profile
                donated_on=form.cleaned_data['donated_on'],
                location=form.cleaned_data['location'],
                units=form.cleaned_data['units'],
                notes=form.cleaned_data.get('notes', ''),
            )
            
            messages.success(
                request,
                f'Donation recorded successfully! Thank you for saving lives. 🩸'
            )
            return redirect('donor:dashboard')
        
        return render(request, 'donor/record_donation.html', {'form': form})


@donor_required
def donation_history(request):
    donations = Donation.objects.filter(donor=request.user)
    context = {
        'donations': donations,
    }
    return render(request, 'donor/donation_history.html', context)