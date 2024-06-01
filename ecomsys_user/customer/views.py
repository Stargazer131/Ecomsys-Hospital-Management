from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer, Account, Fullname, Address
from rest_framework import generics
from customer.serializers import CustomerSerializer


class CustomerLoginAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pass
    
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = Customer.objects.get(account__username=username, account__password=password)
            user_id = user.id
        except Customer.DoesNotExist:
            user_id = -1
        
        response_data = {
            'user_id': user_id
        } 
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    
class CustomerRegisterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pass
    
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        city = request.POST.get('city')
        district = request.POST.get('district')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        
        
        try:
            birthday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
        except Exception as  e:
            birthday_date = None
        
        try:
            user = Customer.objects.get(account__username=username)
            response_data = {
                'success': False
            } 
        
        except Customer.DoesNotExist:
            account = Account(username=username, password=password)
            account.save()
            
            fullname = Fullname(first_name=first_name, last_name=last_name)
            fullname.save()
            
            address = Address(city=city, district=district, street=street, house_number=house_number)
            address.save()
            
            user = Customer(
                account=account, fullname=fullname, address=address,
                email=email, birthday=birthday_date, phone_number=phone_number
            )
            user.save()
            
            response_data = {
                'success': True
            } 
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDestroyView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    