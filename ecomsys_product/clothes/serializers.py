from rest_framework import serializers
from clothes.models import ClothingItem, Manufacturer, Style
from product.serializers import ProductSerializer


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
        
        
class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'
        

class ClothingItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    styles = StyleSerializer(many=True)
    manufacturer = ManufacturerSerializer()
    
    
    class Meta:
        fields = '__all__'
        model = ClothingItem
