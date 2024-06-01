from rest_framework.views import APIView
from rest_framework.response import Response
from payment.models import Payment
from payment.serializers import PaymentSerializer
from rest_framework import status, generics


# Create your views here.
class PaymentMethodListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        response_data = {
            'payment_method_choices': Payment.payment_choice_list
        }

        return Response(response_data, status=status.HTTP_200_OK)


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDestroyView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
