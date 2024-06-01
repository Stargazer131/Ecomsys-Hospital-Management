from rest_framework import serializers
from cart.models import CartItem
import requests


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product_id = representation['product_id']

        url = f'http://localhost:8002/product/{product_id}/'
        response = requests.get(url)
        representation['product'] = response.json()

        return representation

