from django.shortcuts import render
from django.views import View
import requests


# Create your views here.
class SearchByNameView(View):
    template_name = 'product/product_list.html'

    def post(self, request, *args, **kwargs):
        search_type = request.POST.get('searchType')
        product_type = request.POST.get('productType')
        book_fields = request.POST.get('bookFields')
        clothes_fields = request.POST.get('clothesFields')
        mobile_fields = request.POST.get('mobileFields')
        
        text_search = request.POST.get('textSearch')
        voice_search = request.POST.get('voiceSearch')
        image_search_file = request.FILES.get('imageSearch')

        # Prepare the data to be sent in the POST request
        payload = {
            'searchType': search_type,
            'textSearch': text_search,
            'voiceSearch': voice_search,
            'productType': product_type,
            'bookFields': book_fields,
            'clothesFields': clothes_fields,
            'mobileFields': mobile_fields,
        }
        files = {'imageSearch': image_search_file}

        # API URL for the POST request
        api_url = 'http://localhost:8003/search/'
        
        
        response = requests.post(api_url, data=payload, files=files)
        data = response.json()
        return render(request, self.template_name, data)