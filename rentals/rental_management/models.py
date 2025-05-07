from django.db import models

class Property(models.Model):
    ROOM_TYPES = [
        ('Bedsitter', 'Bedsitter'),#first value stored in the database, second value shown to the admin dropdown
        ('1 Bedroom', '1 Bedroom'),
        ('2 Bedroom', '2 Bedroom'),
        ('3 Bedroom', '3 Bedroom'),
    ]  
    name = models.CharField(max_length=255)
    address = models.TextField()
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES, default= 'Bedsitter')
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2) 
    is_rented = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name

class Tenant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='tenants')
    lease_start = models.DateField()  
    lease_end = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class RentalPayment(models.Model):
    PAYMENT_METHOD_CHOICES =[
        ('cash', 'cash'),
        ('bank', 'bank'),
        ('mpesa', 'mpesa'),
        ('cheque', 'cheque'),
        ('other', 'other')
    ]
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payments' )
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_date = models.DateField()
    payment_method= models.CharField(max_length=50,  choices=PAYMENT_METHOD_CHOICES, default='mpesa')
    notes =models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.tenant}"


# Create your models here.
