from django.shortcuts import render
from django.conf import settings
from django.views import View
import requests
from django.conf import settings



# Create your views here.
class ShowCartView(View):
    template_name = 'cart/cart.html'
    api_url = 'http://localhost:8004/cart/'


    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        user_id = request.session.get(settings.USER_ID_KEY)

        if action == 'add':
            product_id = request.POST.get('product_id')
            payload = {
                'action': action,
                'product_id': product_id,
                settings.USER_ID_KEY: user_id
            }
        elif action == 'update':
            cart_item_id = request.POST.get('cart_item_id')
            quantity = request.POST.get('quantity')
            payload = {
                'action': action,
                'cart_item_id': cart_item_id,
                'quantity': quantity,
                settings.USER_ID_KEY: user_id
            }
        else:
            cart_item_id = request.POST.get('cart_item_id')
            payload = {
                'action': action,
                'cart_item_id': cart_item_id,
                settings.USER_ID_KEY: user_id
            }

        response = requests.post(self.api_url, data=payload)
        data = response.json()
        return render(request, self.template_name, data)


    def get(self, request, *args, **kwargs):
        user_id = request.session.get(settings.USER_ID_KEY)
        response = requests.get(self.api_url, params={settings.USER_ID_KEY: user_id})
        
        data = response.json()
        return render(request, self.template_name, data)