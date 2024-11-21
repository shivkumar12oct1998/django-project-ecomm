from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('book/',views.book_view),
     path('book/<int:pk>/', views.book_delete_view, name='book-delete'),
     path('home/',views.home,name="home"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    #path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_details/', views.cart_details, name='cart_details'),
     path('proceed_checkout/', views.proceed_checkout, name='proceed_checkout'),  # Add this line
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('payment/', views.payment, name='payment'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]

