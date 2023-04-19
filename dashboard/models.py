from django.db import models
from django.contrib.auth.models import User
from user.models import Profile


# Create your models here.
CATEGORY =(
('Fire Equipments','Fire Equipments'),
('Rescue','Rescue'),
('Repairing Equipments','Repairing Equipments'),
)





class Product(models.Model):
    name = models.CharField(max_length=100, null= True)
    category = models.CharField(max_length=20, choices= CATEGORY, null= True)
    quantity = models.PositiveIntegerField(null= True)
    unit_price = models.PositiveBigIntegerField(null=True)
    class Meta:
        verbose_name_plural ='Product'
    def __str__(self):
        # return f'{self.name}-{self.quantity}
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null= True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
    
class Invoice(models.Model):
    invoice_date = models.DateField(null=False, blank=False)
    customer_name = models.CharField(max_length=25, null=False, blank=False)
    customer_phone = models.CharField(max_length=15, null=False, blank=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0, blank=False, null=False)
    quantity = models.IntegerField(default=0, blank=False, null=False)
    staff = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    total = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.customer_name
    
class InvoiceBills(models.Model):
    invoice_id = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    bill = models.FileField(upload_to='bills') 
