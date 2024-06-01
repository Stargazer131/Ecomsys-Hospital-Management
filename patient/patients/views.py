from rest_framework import generics
from patients.models import Patient, MedicalRecord, LabTest, Prescription, Treatment
from patients.serializers import PatientSerializer, MedicalRecordSerializer, LabTestSerializer, PrescriptionSerializer, TreatmentSerializer

# Patient Views


class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientCreateAPIView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientUpdateAPIView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDestroyAPIView(generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# MedicalRecord Views


class MedicalRecordListAPIView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class MedicalRecordRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class MedicalRecordCreateAPIView(generics.CreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class MedicalRecordUpdateAPIView(generics.UpdateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class MedicalRecordDestroyAPIView(generics.DestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

# LabTest Views


class LabTestListAPIView(generics.ListAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer


class LabTestRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer


class LabTestCreateAPIView(generics.CreateAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer


class LabTestUpdateAPIView(generics.UpdateAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer


class LabTestDestroyAPIView(generics.DestroyAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

# Prescription Views


class PrescriptionListAPIView(generics.ListAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionCreateAPIView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionUpdateAPIView(generics.UpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

# Treatment Views


class TreatmentListAPIView(generics.ListAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentCreateAPIView(generics.CreateAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentDestroyAPIView(generics.DestroyAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
