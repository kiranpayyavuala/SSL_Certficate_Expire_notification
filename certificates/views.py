from django.shortcuts import render, redirect
from .models import SSLCertificate
from .forms import SSLCertificateForm
from django.db.models.functions import TruncMonth, TruncYear  # Add these imports
from django.db.models import Count
from datetime import datetime, timedelta

def certificate_list(request):
    sort_by_days = request.GET.get('sort_by_days', 'asc')
    if sort_by_days == 'asc':
        certificates = SSLCertificate.objects.all().order_by('expire_date')
    else:
        certificates = SSLCertificate.objects.all().order_by('-expire_date')
    
    total_certificates = certificates.count()
    valid_certificates = certificates.filter(status='active').count()
    expiring_soon = certificates.filter(expire_date__lte=datetime.now() + timedelta(days=15)).count()
    expired_certificates = certificates.filter(status='inactive').count()

    context = {
        'certificates': certificates,
        'sort_by_days': sort_by_days,
        'total_certificates': total_certificates,
        'valid_certificates': valid_certificates,
        'expiring_soon': expiring_soon,
        'expired_certificates': expired_certificates,
    }
    return render(request, 'certificates/certificate_list.html', context)

def add_certificate(request):
    if request.method == 'POST':
        form = SSLCertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = SSLCertificateForm()
    return render(request, 'certificates/add_certificate.html', {'form': form})

def certificate_expiration_counts(request):
    current_year = datetime.now().year
    next_year = current_year + 1

    monthly_counts = SSLCertificate.objects.annotate(month=TruncMonth('expire_date')).values('month').annotate(count=Count('id')).order_by('month')
    yearly_counts = SSLCertificate.objects.annotate(year=TruncYear('expire_date')).values('year').annotate(count=Count('id')).order_by('year')

    context = {
        'monthly_counts': monthly_counts,
        'yearly_counts': yearly_counts,
    }
    return render(request, 'certificates/certificate_expiration_counts.html', context)
