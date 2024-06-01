from rest_framework import serializers
from patients.models import Patient, MedicalRecord, LabTest, Prescription, Treatment


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalRecord
        fields = '__all__'


class LabTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LabTest
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = '__all__'


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatment
        fields = '__all__'
