from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import book
from .serializer import serializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import book
from django.http import HttpResponse
@api_view(['GET','POST'])
def book_view(request):
    if request.method=='GET':
       m=book.objects.all()
       serializer1=serializer(m,many=True)
       return Response(serializer1.data)
    if request.method=='POST':
        serializer2 = serializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def book_delete_view(request, pk):
    book1 = get_object_or_404(book, pk=pk)
    if request.method == 'DELETE':
        book1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
def home(request):
    bo = book.objects.all()
    return render(request, 'home.html', {'bo': bo})


#def product(request):
    #return render(request,'product.html')

# Create your views here.

def product_detail(request, product_id):
    product = get_object_or_404(book, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

#def add_to_cart(request, product_id):
    
   # product = get_object_or_404(book, pk=product_id)

    
    #product_price = float(product.price)

    
    #cart = request.session.get('cart', {})

    
    #if str(product.id) in cart:
        #cart[str(product.id)]['quantity'] += 1
    #else:
        
        #cart[str(product.id)] = {
          #  'name': product.name,
           # 'price': product_price,  # Store as float
            #'image': product.image.url,
            #'quantity': 1
        #}

    
    #request.session['cart'] = cart

    
    #return redirect('cart_details')

# views.py


def clear_cart(request):
    # Clear the cart from the session
    request.session['cart'] = []

    # Redirect to the checkout success page
    return redirect('checkout_success')









def add_to_cart(request, product_id):
    # Fetch the product object
    product = get_object_or_404(book, id=product_id)

    # Check if the stock is greater than 0 before allowing the user to add it to the cart
    if product.stock > 0:
        # Decrease stock by 1
        product.stock -= 1
        product.save()

        # Get the cart from the session, defaulting to an empty list if it doesn't exist
        cart = request.session.get('cart', [])

        # Ensure the cart is a list of dictionaries
        if not isinstance(cart, list):
            cart = []

        # Check if the product is already in the cart
        product_in_cart = next((item for item in cart if item['id'] == product.id), None)

        if product_in_cart:
            # If the product is already in the cart, update the quantity and total price
            product_in_cart['quantity'] += 1
            product_in_cart['total_price'] = product_in_cart['quantity'] * float(product.price)
        else:
            # If the product is not in the cart, append it as a new item
            cart.append({
                'id': product.id,
                'name': product.name,
                'price': str(product.price),
                'quantity': 1,
                'total_price': str(product.price),
                'image': product.image.url
            })

        # Save the updated cart back to the session
        request.session['cart'] = cart

        # Redirect to the cart details page
        return redirect('cart_details')  # This is where the user will be redirected after adding the item to the cart
    else:
        return HttpResponse('Sorry, this product is out of stock!', status=400)
#def cart_details(request):
    
   # cart = request.session.get('cart', {})

    
    #for item in cart.values():
        #item['total_price'] = item['price'] * item['quantity']  # Calculate total for each product

    
    #total_price = sum(item['total_price'] for item in cart.values())

    
    #return render(request, 'cart_details.html', {'cart': cart, 'total_price': total_price})






def cart_details(request):
    # Retrieve the cart from the session
    cart = request.session.get('cart', [])

    # Calculate total price of the cart
    total_price = sum(float(item['total_price']) for item in cart)

    return render(request, 'cart_details.html', {
        'cart': cart,
        'total_price': total_price
    })

def proceed_checkout(request):
    # This view will clear the cart when the "Proceed to Checkout" button is clicked
    if request.method == 'POST':
        # Clear the cart by removing it from the session
        request.session['cart'] = {}

        # Optionally, you can redirect to a success or checkout page
        return redirect('checkout_success')  # Redirect to a checkout or success page

    # If it's not a POST request, we can redirect back to the cart page
    return redirect('cart_details')

def checkout_success(request):
    # A simple page to confirm the cart is cleared and proceed with checkout
    return render(request, 'checkout_success.html')



def payment(request):
    # Logic for payment page (can be a simple placeholder for now)
    return render(request, 'payment.html')