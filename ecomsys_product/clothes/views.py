from rest_framework import generics
from clothes.models import ClothingItem
from clothes.serializers import ClothingItemSerializer


class ClothingItemListView(generics.ListAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class ClothingItemRetrieveView(generics.RetrieveAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class ClothingItemCreateView(generics.CreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class ClothingItemUpdateView(generics.UpdateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class ClothingItemDestroyView(generics.DestroyAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
    