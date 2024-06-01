from rest_framework import generics
from .models import Staff, Manager, Receptionist
from .serializers import StaffSerializer, ManagerSerializer, ReceptionistSerializer

# Staff Views


class StaffListAPIView(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffCreateAPIView(generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffUpdateAPIView(generics.UpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDestroyAPIView(generics.DestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

# Manager Views


class ManagerListAPIView(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerCreateAPIView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerUpdateAPIView(generics.UpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerDestroyAPIView(generics.DestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

# Receptionist Views


class ReceptionistListAPIView(generics.ListAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer


class ReceptionistRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer


class ReceptionistCreateAPIView(generics.CreateAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer


class ReceptionistUpdateAPIView(generics.UpdateAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer


class ReceptionistDestroyAPIView(generics.DestroyAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer
