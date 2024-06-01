from rest_framework import serializers
from .models import Building, Room, Bed, Furniture, MedicalEquipment


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'


class MedicalEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalEquipment
        fields = '__all__'
