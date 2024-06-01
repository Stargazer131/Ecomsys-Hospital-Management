import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from order.models import Order
from order.serializers import OrderSerializer
from django.conf import settings


# Create your views here.
class PlaceOrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get(settings.USER_ID_KEY)

        shipping_address = request.POST.get("shipping_address")
        shipping_method = request.POST.get("shipping_method")

        payment_method = request.POST.get("payment_method")
        card_number = request.POST.get("card_number")
        expired_date = request.POST.get("expired_date")
        security_code = request.POST.get("security_code")

        # process
        url = 'http://localhost:8004/cart/'
        response = requests.get(url, params={settings.USER_ID_KEY: user_id})
        cart_items = response.json()['cart_items']

        total_price = 0
        for item in cart_items:
            total_price += item['total_price']

        # create order
        order = Order(user_id=user_id, total_price=total_price)
        order.save()

        # update cart item
        url = 'http://localhost:8004/cart/cart-item/update/'
        payload = {
            settings.USER_ID_KEY: user_id,
            'order_id': order.pk,
        }
        response = requests.post(url, json=payload)

        # create shipment
        url = 'http://localhost:8006/shipment/create/'
        payload = {
            'order_id': order.pk,
            'shipping_address': shipping_address,
            'shipping_method': shipping_method,
        }
        response = requests.post(url, json=payload)
        shipment = response.json()

        # create payment
        total_amount = total_price + shipment['fee']
        url = 'http://localhost:8007/payment/create/'
        if card_number is None or card_number == '':
            payload = {
                'order_id': order.pk,
                'method': payment_method,
                'total_amount': total_amount,
            }
        else:
            payload = {
                'order_id': order.pk,
                'method': payment_method,
                'card_number': card_number,
                'expired_date': expired_date,
                'security_code': security_code,
                'total_amount': total_amount,
            }
        response = requests.post(url, json=payload)
        payment = response.json()
        print(payment)

        response_data = {
            'created_status': 'successfully'
        }

        return Response(response_data, status=status.HTTP_200_OK)


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDestroyView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
