from django.shortcuts import render
from django.views import View
import requests
# Create your views here.


class ProductListView(View):
    template_name = 'product/product_list.html'

    def get(self, request, *args, **kwargs):
        api_url = 'http://localhost:8002/product/all/'

        response = requests.get(api_url)
        data = response.json()
        context = {
            'products': data,
        }
        return render(request, self.template_name, context)