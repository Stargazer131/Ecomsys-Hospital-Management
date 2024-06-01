from rest_framework import serializers
from general.models import Staff, Manager, Receptionist


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    
    class Meta:
        model = Manager
        fields = '__all__'


class ReceptionistSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    
    class Meta:
        model = Receptionist
        fields = '__all__'
