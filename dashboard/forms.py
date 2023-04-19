from django import forms
from .models import Product, Order, Invoice

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category', 'quantity', 'unit_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']

class InvoiceForm(forms.Form):
    class Meta:
        model = Invoice
        fields = '__all__'
