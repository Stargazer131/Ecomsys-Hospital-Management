from rest_framework import serializers
from mobile.models import MobileType, Mobile
from product.serializers import ProductSerializer
from clothes.serializers import ManufacturerSerializer
        
        
class MobileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileType
        fields = '__all__'
        

class MobileSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    mobile_type = MobileTypeSerializer()
    manufacturer = ManufacturerSerializer()
    
    
    class Meta:
        fields = '__all__'
        model = Mobile
