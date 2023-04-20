from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, InvoiceBills, Invoice, Profile
from .forms import ProductForm,OrderForm, InvoiceForm
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.contrib import messages
import os
from django.db.models import Q

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
           
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('dashboard-products')
    
    elif request.method == 'GET':
        items = Product.objects.filter(
            Q(name__icontains=q) |
            Q(category__icontains=q)
        )
        form = ProductForm()
        # items = Product.objects.all()
        context={
            'items': items,
            'form': form,
        }
        return render(request, 'dashboard/products.html', context)
    else:
        form = ProductForm()
        items = Product.objects.all()
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    if request.method == 'GET':
        orders = Order.objects.filter(
            Q(date__icontains=q)
        )
        print('new')
        print(orders)
        context={
            'orders': orders,
        }
        return render(request, 'dashboard/orders.html', context)
    else:
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



def invoice(request):
    if request.method == 'POST':
        # Process the form data to create a new invoice
        invoice_date = request.POST.get('invoice_date')
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        product_id = request.POST.get('product_id')
        rate = request.POST.get('rate')
        quantity = request.POST.get('quantity')
        staff_id = request.POST.get('staff_id')
        
        # Perform validation checks on the form data
        # ...
        
        # Create a new invoice object and save it to the database
        product = Product.objects.get(id=product_id)
        staff = Profile.objects.get(id=staff_id)
        total = rate * quantity
        invoice = Invoice.objects.create(
            invoice_date=invoice_date,
            customer_name=customer_name,
            customer_phone=customer_phone,
            product=product,
            rate=rate,
            quantity=quantity,
            staff=staff,
            total=total,
        )
        
        # Redirect the user to a success page or display a success message
        # ...
    
    else:
        # Render the template for creating a new invoice
        products = Product.objects.all()
        staffs = Profile.objects.all()
        context = {
            'products': products,
            'staffs': staffs,
        }
        return render(request, 'dashboard/invoice.html', context)


# def createReceipt(pk):
#     store_name= "Sajilo Inventory"

#     # correct store details
#     location = "Kathmandu, Nepal"
#     store_tel = "01-3425342"

#     bill = Invoice.objects.get(id = pk)
#     fileName = bill.customer_name + ".txt"
    
#     receipt = open(fileName, "w+")
#     receipt.write(f"\t\t{store_name.title()}\n")
#     receipt.write(f"\t\t{location}\n")
#     receipt.write(f"\t\t{store_tel}\n\n\n")

#     receipt.write(f"Bill no: {bill.id}\n")
#     receipt.write(f"Date: {bill.invoice_date}\n")

#     receipt.write("-" * 47)
#     receipt.write(f"\nProduct \t\t Qty \t Rate \t Amount\n")
#     receipt.write("-" * 47)

#     for product in bill:
#         receipt.write(f"\n{product.product} \t\t {product.quantity} \t {product.rate} \t {product.total}")

#     receipt.write(f"\n" + "-" * 47)
#     receipt.close()

#     InvoiceBills.objects.create(
#         invoice_id = bill.id,
#         bill = receipt
#     )


# def generateInvoice(request):
 
 #      form = InvoiceForm()

  #     if request.method == 'POST':
   #         form = InvoiceForm(request.POST)
    #        if form.is_valid():
     #         form.save()
      #        messages.success(request, 'Invoice added successfully.')
       #       bill = Invoice.objects.latest('id')
        #        createReceipt(bill.id)
                        # Add url here
         #       return redirect('invoice')

#     invoiceData = Invoice.objects.all()
#     context = {'invoice_data': invoiceData}

#     #add url here
#     return render(request, 'dashboard/invoice.html', context)



# def generateBill(request, pk):
#     bill = Invoice.objects.get(id = pk)
#     fileName = bill.customer_name + ".txt"

#     file_path = fileName
#     os.startfile(file_path, 'print')
#     return redirect("route:invoice")


# def searchProd(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#     print('query')
#     print(q)

#     if q:
#         # query = request.GET['q']
#         items = Product.objects.filter(
#             Q(name__icontains=q) |
#             Q(category__icontains=q)
#         )
#     elif q == '':
#         items = Product.objects.all()

    
#     print(products)
#     print('after')

#     form = ProductForm()

#     context = {
#         'products': items,
#         'form': form,
#     }
    
#     return render(request, 'dashboard/products.html', context)

# def searchInvoice(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''

#     invoice = Invoice.objects.filter(
#         Q(invoice_date__icontains=q)
#     )

#     context = {'invoice': invoice}
    
#     # Add url
#     return render(request, 'search', context)



# # QR code scanner

import cv2
from pyzbar.pyzbar import decode
import json

def qr_scanner(request):
    cap = cv2.VideoCapture(0)
    qr_code_detected = False
    data = []

    while True:
        ret, frame = cap.read()

        qr_codes = decode(frame)
        
        for qr_code in qr_codes:
            print(qr_code.data.decode('utf-8'))
            data.append(qr_code.data.decode('utf-8'))
            print(data)
            qr_code_detected = True
            break
        
        cv2.imshow('frame', frame)
        
        if qr_code_detected or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


    json_data = json.loads(data[0])

    name = json_data['name']
    quantity = json_data['quantity']
    category = json_data['category']
    unit_price = json_data['unit-price']

    product = Product.objects.filter(name=name, category=category, unit_price=unit_price).first()

    if product:
        product.quantity += quantity
        product.save()
    else:
        Product.objects.create(
            name=name,
            category=category,
            quantity=quantity,
            unit_price=unit_price
        )

    items = Product.objects.all()
    form = ProductForm()

    context={
        'items': items,
        'form': form,
    }
    
    return render(request, 'dashboard/products.html', context)
