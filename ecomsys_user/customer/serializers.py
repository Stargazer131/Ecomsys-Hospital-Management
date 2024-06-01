from rest_framework import serializers
from customer.models import Customer, Account, Address, Fullname


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
        
class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = '__all__'
        
        
class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    account = AccountSerializer()
    fullname = FullnameSerializer()
    
    
    class Meta:
        model = Customer
        fields = '__all__'
        
        