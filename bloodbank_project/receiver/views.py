from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.decorators import receiver_required
from .models import BloodRequest
from .forms import BloodRequestForm


@receiver_required
def dashboard(request):
    user = request.user
    requests = BloodRequest.objects.filter(receiver=user)

    total_requests = requests.count()
    pending_requests = requests.filter(status='pending').count()
    fulfilled_requests = requests.filter(status='fulfilled').count()
    rejected_requests = requests.filter(status='rejected').count()

    context = {
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'fulfilled_requests': fulfilled_requests,
        'rejected_requests': rejected_requests,
        'recent_requests': requests[:5],
    }
    return render(request, 'receiver/dashboard.html', context)


@receiver_required
def create_request(request):
    if request.method == 'GET':
        form = BloodRequestForm()
        return render(request, 'receiver/create_request.html', {'form': form})

    if request.method == 'POST':
        form = BloodRequestForm(request.POST)

        if form.is_valid():
            BloodRequest.objects.create(
                receiver=request.user,
                blood_type=form.cleaned_data['blood_type'],
                units=form.cleaned_data['units'],
                urgency=form.cleaned_data['urgency'],
                hospital=form.cleaned_data['hospital'],
                reason=form.cleaned_data['reason'],
                notes=form.cleaned_data.get('notes', ''),
            )

            messages.success(
                request,
                'Blood request submitted successfully! We will process it shortly.'
            )
            return redirect('receiver:dashboard')

        return render(request, 'receiver/create_request.html', {'form': form})


@receiver_required
def request_history(request):
    requests = BloodRequest.objects.filter(receiver=request.user)
    context = {
        'requests': requests,
    }
    return render(request, 'receiver/request_history.html', context)