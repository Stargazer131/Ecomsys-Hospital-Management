import copy
from django.shortcuts import render
from django.views import View
from django.conf import settings
import requests


# Create your views here.
class PlaceOrderView(View):
    template_name = 'order/order.html'
    order_api_url = 'http://localhost:8005/order/create/'
    cart_item_api_url = 'http://localhost:8004/cart/'
    shipment_method_api_url = 'http://localhost:8006/shipment/method/all/'
    payment_method_api_url = 'http://localhost:8007/payment/method/all/'
    

    def get(self, request, *args, **kwargs):
        # cart
        user_id = request.session.get(settings.USER_ID_KEY)
        response = requests.get(self.cart_item_api_url, params={settings.USER_ID_KEY: user_id})
        cart_item_data = response.json()
        total_price = 0
        for cart_item in cart_item_data['cart_items']:
            total_price += float(cart_item['total_price'])

        # shipment
        response = requests.get(self.shipment_method_api_url)
        shipping_choices = response.json()
        shipping_choices_data = shipping_choices["shipping_choices"]
        shipping_method_choices = [key for key in shipping_choices_data.keys()]
        
        # payment
        response = requests.get(self.payment_method_api_url)
        payment_method_choices = response.json()
        
        data = {
            "order_items": cart_item_data['cart_items'],
            "shipping_method_choices": shipping_method_choices,
            "payment_method_choices": payment_method_choices['payment_method_choices'],
            "total_price": total_price,
        }

        return render(request, self.template_name, data)
    
    
    def post(self, request, *args, **kwargs):
        user_id = request.session.get(settings.USER_ID_KEY)
        
        shipping_address = request.POST.get('shipping_address')
        shipping_method = request.POST.get('shipping_method')
        
        payment_method = request.POST.get('payment_method')
        card_number = request.POST.get('card_number')
        expired_date = request.POST.get('expired_date')
        security_code = request.POST.get('security_code')
        
        data = {
            'user_id': user_id,
            'shipping_address': shipping_address,
            'shipping_method': shipping_method,
            'payment_method': payment_method,
            'card_number': card_number,
            'expired_date': expired_date,
            'security_code': security_code
        }
        
        
        response = requests.post(self.order_api_url, data=data)
        response_data = response.json()     
        if response_data.get('created_status') == 'successfully':
            return render(request, 'order/thank_you.html')
        else:
            pass