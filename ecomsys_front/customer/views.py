from django.shortcuts import redirect, render
from django.conf import settings
from django.views import View
import requests


class LoginView(View):
    template_name = 'customer/login.html'
    api_url = 'http://localhost:8001/customer/login/'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        payload = {
            'username': username,
            'password': password,
            'login_failed': False
        }
        
        print(payload)
        
        response = requests.post(self.api_url, data=payload)
        data = response.json()
        user_id = data.get('user_id')
        if user_id == -1:
            payload['login_failed'] = True
            return render(request, self.template_name, payload)
        else:
            request.session[settings.USER_ID_KEY] = user_id
            return redirect('product_list')


class RegisterView(View):
    template_name = 'customer/register.html'
    api_url = 'http://localhost:8001/customer/register/'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
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
        
        
        payload = {
            'username': username,
            'password': password,
            'birthday': birthday,
            'email': email,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'city': city,
            'district': district,
            'street': street,
            'house_number': house_number,
        }
                        
        response = requests.post(self.api_url, data=payload)
        data = response.json()
        success = data.get('success')
        if success:
            return render(request, self.template_name, {"message" : "Register completed"})
        else:
            payload['message'] = 'Register failed, username already existed'
            return render(request, self.template_name, payload)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return redirect('login')