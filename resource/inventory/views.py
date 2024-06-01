from rest_framework import generics
from .models import Manufacturer, Resource, Bill, Medication, Supply, BillItem
from .serializers import ManufacturerSerializer, ResourceSerializer, BillSerializer, MedicationSerializer, SupplySerializer, BillItemSerializer

# Manufacturer Views


class ManufacturerListAPIView(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerCreateAPIView(generics.CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerUpdateAPIView(generics.UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerDestroyAPIView(generics.DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

# Resource Views


class ResourceListAPIView(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceCreateAPIView(generics.CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceUpdateAPIView(generics.UpdateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceDestroyAPIView(generics.DestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# Bill Views


class BillListAPIView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillCreateAPIView(generics.CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillUpdateAPIView(generics.UpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDestroyAPIView(generics.DestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

# Medication Views


class MedicationListAPIView(generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationCreateAPIView(generics.CreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationUpdateAPIView(generics.UpdateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicationDestroyAPIView(generics.DestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

# Supply Views


class SupplyListAPIView(generics.ListAPIView):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class SupplyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class SupplyCreateAPIView(generics.CreateAPIView):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class SupplyUpdateAPIView(generics.UpdateAPIView):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class SupplyDestroyAPIView(generics.DestroyAPIView):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

# BillItem Views


class BillItemListAPIView(generics.ListAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer


class BillItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer


class BillItemCreateAPIView(generics.CreateAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer


class BillItemUpdateAPIView(generics.UpdateAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer


class BillItemDestroyAPIView(generics.DestroyAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
