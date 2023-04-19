from django.urls import path
from .import views


urlpatterns = [

    path(' dashboard/', views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('products/',views.products, name='dashboard-products'),
    path('orders/',views.orders, name='dashboard-orders'),
    path('products/delete/<int:pk>/',views.product_delete, name='dashboard-product-delete'),
    path('products/update/<int:pk>/',views.product_update, name='dashboard-product-update'),

    # path('invoice/', views.invoice, name="invoice"),
    # path('save', views.generateBill, name="generate-bill"),
    # path('search-prod', views.searchProd, name="search-prod"),
    # path('search-invoice', views.searchInvoice, name="search-invoice"),

    path('scan-product/', views.qr_scanner, name="scan"),


]

