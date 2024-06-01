from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cart import cart
from cart.serializers import CartItemSerializer
from django.conf import settings


class CartListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get(settings.USER_ID_KEY)
        cart_items = cart.get_cart_items(user_id)          
        serializer = CartItemSerializer(cart_items, many=True)
        response_data = {
            'cart_items': serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        user_id = request.POST.get(settings.USER_ID_KEY)
        
        if action == 'add':
            product_id = int(request.POST.get('product_id'))
            cart.add_to_cart(product_id, user_id)
            
        elif action == 'update':
            cart_item_id = int(request.POST.get('cart_item_id'))
            quantity = int(request.POST.get('quantity'))            
            cart.update_cart(cart_item_id, quantity)
            
        else:
            cart_item_id = int(request.POST.get('cart_item_id'))
            cart.remove_from_cart(cart_item_id)
        
        cart_items = cart.get_cart_items(user_id)          
        serializer = CartItemSerializer(cart_items, many=True)
        response_data = {
            'cart_items': serializer.data
        } 
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    
class CartItemAPIView(APIView):    
    def post(self, request, *args, **kwargs):
        user_id = request.data.get(settings.USER_ID_KEY)
        order_id = request.data.get('order_id')
        
        cart_items = cart.get_cart_items(user_id) 
        for item in cart_items:
            item.order_id = order_id
            item.save()
                 
        response_data = {
            'success': True
        } 
        
        return Response(response_data, status=status.HTTP_200_OK)