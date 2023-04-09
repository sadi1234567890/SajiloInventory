from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm
from django.contrib.auth.models import User
from django.forms import formset_factory
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders =Order.objects.all()
    context={
        'orders': orders,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context={
        'workers': workers
    }
    return render(request, 'dashboard/staff.html', context)


@login_required(login_url='user-login')
def products(request):
    items = Product.objects.all()

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('dashboard-products')

    else:
        form = ProductForm()
    context={
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/products.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-products')

    return render(request, 'dashboard/product_delete.html')

@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required(login_url='user-login')
def orders(request):
    orders= Order.objects.all()
    
    context={
        'orders': orders,
    }
    return render(request, 'dashboard/orders.html', context)


def add_orders(request):
    OrderFormSet = formset_factory(OrderForm, extra=5)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                # process each form in the formset
                pass
            messages.success(request, 'Orders added successfully.')
            return redirect('orders')
        else:
            messages.error(request, 'There was an error with your form submission.')
    else:
        formset = OrderFormSet()
    context = {
        'formset': formset,
    }
    return render(request, 'dashboard/add_orders.html', context)