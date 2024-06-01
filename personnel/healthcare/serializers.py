from rest_framework import serializers
from healthcare.models import Doctor, Nurse, Pharmacist, LabTechnician
from general.serializers import StaffSerializer


class DoctorSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    
    class Meta:
        model = Doctor
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    
    class Meta:
        model = Nurse
        fields = '__all__'


class PharmacistSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    
    class Meta:
        model = Pharmacist
        fields = '__all__'


class LabTechnicianSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    
    class Meta:
        model = LabTechnician
        fields = '__all__'
