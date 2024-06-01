from rest_framework.views import APIView
from rest_framework.response import Response
from shipment.models import Shipment
from rest_framework import status, generics
from shipment.serializers import ShipmentSerializer


# Create your views here.
class ShipmentMethodListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        response_data = {
            'shipping_choices': Shipment.shipping_methods
        }

        return Response(response_data, status=status.HTTP_200_OK)


class ShipmentListView(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentRetrieveView(generics.RetrieveAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentCreateView(generics.CreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentUpdateView(generics.UpdateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentDestroyView(generics.DestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
