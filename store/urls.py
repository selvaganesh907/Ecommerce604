from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('vendor/',views.vendor,name='vendor'),
    path('customer/',views.customer,name='customer'),
    path('upload/',views.product_upload,name='upload'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
]