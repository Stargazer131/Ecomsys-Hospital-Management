from rest_framework import serializers
from users.models import Fullname, Address, Role, Account, User


class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    fullname = FullnameSerializer()
    address = AddressSerializer()
    role = RoleSerializer(required=False)

    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        # Extract nested data
        account_data = validated_data.pop('account')
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')
        role_data = validated_data.pop('role', None)  # Use pop with default None for optional field

        # Create nested objects
        account = Account.objects.create(**account_data)
        fullname = Fullname.objects.create(**fullname_data)
        address = Address.objects.create(**address_data)

        if role_data:
            role = Role.objects.create(**role_data)
        else:
            role = None

        # Create the user
        user = User.objects.create(account=account, fullname=fullname, address=address, role=role, **validated_data)

        return user
