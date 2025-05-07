from django.shortcuts import render
from .models import Property, Tenant, RentalPayment
from django.utils import  timezone
from datetime import timedelta


def dashboard(request):#create a view function called dashboard
    total_properties = Property.objects.count()
    rented_properties = Property.objects.filter(is_rented=True).count()
    vacant_properties = Property.objects.filter(is_rented=False).count()
    total_tenants =Tenant.objects.count()
    total_payments = RentalPayment.objects.count()
    recent_payments = RentalPayment.objects.order_by('-payment_date')[:5]
    lease_ending_soon = Tenant.objects.filter(lease_end__lte=timezone.now().date() + timedelta(days=30))




    context = {
        'total_properties': total_properties,
        'rented_properties':rented_properties,
        'vacant_properties': vacant_properties,
        'total_tenants': total_tenants,
        'total_payments': total_payments,
        'recent_payments': recent_payments,
        'lease_ending_soon': lease_ending_soon,
    }
    return render(request, 'dashboard.html', context)

def all_properties(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, 'all_properties.html', context)

def vacant_properties(request):
    vacant_properties= Property.objects.filter(is_rented=False)
    context = {
        'vacant_properties': vacant_properties
    }
    return render(request, 'vacant_properties.html', context )

def tenants_list(request):
    tenants = Tenant.objects.all()
    context ={
        'tenants': tenants
    }
    return render(request, 'tenants_list.html', context)
# Create your views here.
