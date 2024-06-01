from rest_framework import generics
from .models import Doctor, Nurse, Pharmacist, LabTechnician
from .serializers import DoctorSerializer, NurseSerializer, PharmacistSerializer, LabTechnicianSerializer

# Doctor Views


class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorCreateAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorUpdateAPIView(generics.UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDestroyAPIView(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# Nurse Views


class NurseListAPIView(generics.ListAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer


class NurseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer


class NurseCreateAPIView(generics.CreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer


class NurseUpdateAPIView(generics.UpdateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer


class NurseDestroyAPIView(generics.DestroyAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

# Pharmacist Views


class PharmacistListAPIView(generics.ListAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer


class PharmacistRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer


class PharmacistCreateAPIView(generics.CreateAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer


class PharmacistUpdateAPIView(generics.UpdateAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer


class PharmacistDestroyAPIView(generics.DestroyAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer

# LabTechnician Views


class LabTechnicianListAPIView(generics.ListAPIView):
    queryset = LabTechnician.objects.all()
    serializer_class = LabTechnicianSerializer


class LabTechnicianRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LabTechnician.objects.all()
    serializer_class = LabTechnicianSerializer


class LabTechnicianCreateAPIView(generics.CreateAPIView):
    queryset = LabTechnician.objects.all()
    serializer_class = LabTechnicianSerializer


class LabTechnicianUpdateAPIView(generics.UpdateAPIView):
    queryset = LabTechnician.objects.all()
    serializer_class = LabTechnicianSerializer


class LabTechnicianDestroyAPIView(generics.DestroyAPIView):
    queryset = LabTechnician.objects.all()
    serializer_class = LabTechnicianSerializer
