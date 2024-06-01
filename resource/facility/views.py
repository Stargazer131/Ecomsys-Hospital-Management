from rest_framework import generics
from .models import Building, Room, Bed, Furniture, MedicalEquipment
from .serializers import BuildingSerializer, RoomSerializer, BedSerializer, FurnitureSerializer, MedicalEquipmentSerializer

# Building Views


class BuildingListAPIView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingCreateAPIView(generics.CreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingUpdateAPIView(generics.UpdateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingDestroyAPIView(generics.DestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

# Room Views


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCreateAPIView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomUpdateAPIView(generics.UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDestroyAPIView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# Bed Views


class BedListAPIView(generics.ListAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedCreateAPIView(generics.CreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedUpdateAPIView(generics.UpdateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedDestroyAPIView(generics.DestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

# Furniture Views


class FurnitureListAPIView(generics.ListAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class FurnitureRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class FurnitureCreateAPIView(generics.CreateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class FurnitureUpdateAPIView(generics.UpdateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class FurnitureDestroyAPIView(generics.DestroyAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

# MedicalEquipment Views


class MedicalEquipmentListAPIView(generics.ListAPIView):
    queryset = MedicalEquipment.objects.all()
    serializer_class = MedicalEquipmentSerializer


class MedicalEquipmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MedicalEquipment.objects.all()
    serializer_class = MedicalEquipmentSerializer


class MedicalEquipmentCreateAPIView(generics.CreateAPIView):
    queryset = MedicalEquipment.objects.all()
    serializer_class = MedicalEquipmentSerializer


class MedicalEquipmentUpdateAPIView(generics.UpdateAPIView):
    queryset = MedicalEquipment.objects.all()
    serializer_class = MedicalEquipmentSerializer


class MedicalEquipmentDestroyAPIView(generics.DestroyAPIView):
    queryset = MedicalEquipment.objects.all()
    serializer_class = MedicalEquipmentSerializer
