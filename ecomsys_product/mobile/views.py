from rest_framework import generics
from mobile.models import Mobile
from mobile.serializers import MobileSerializer


class MobileListView(generics.ListAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileRetrieveView(generics.RetrieveAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileCreateView(generics.CreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileUpdateView(generics.UpdateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MobileDestroyView(generics.DestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
