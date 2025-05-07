from django.contrib import admin
from .models import Property
from .models import Tenant
from .models import RentalPayment



@admin.register(Property)



class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'room_type', 'monthly_rent', 'is_rented')
    list_filter = ('room_type', 'is_rented')
    search_fields = ('name', "address")

@admin.register(Tenant)

class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'lease_start')
    list_filter = ('lease_start', 'lease_end')
    search_fields =('first_name', 'last_name', 'email')

@admin.register(RentalPayment)

class RentalPaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'amount', 'payment_date', 'payment_method')
    list_filter = ('payment_method', 'payment_date')
    search_filters = ('tenant__first_name', 'tenant_last_name', 'amount')

# Register your models here.
