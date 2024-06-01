from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from search.image_recommender import predict_similar_image
from search.image_recommender import get_image_features_list


class SearchByNameAPIView(APIView):
    def post(self, request, *args, **kwargs):
        search_type = request.POST.get('searchType')
        
        product_type = request.POST.get('productType')
        book_fields = request.POST.get('bookFields')
        clothes_fields = request.POST.get('clothesFields')
        mobile_fields = request.POST.get('mobileFields')
        
        text_search = request.POST.get('textSearch')
        image_search = request.FILES.get('imageSearch')
        voice_search = request.POST.get('voiceSearch')

        if product_type == 'all':
            result = self.search_product(search_type, text_search, voice_search, image_search)
        if product_type == 'book':
            result = self.search_book(search_type, text_search, voice_search, image_search, book_fields)
        if product_type == 'clothes':
            result = self.search_clothes(search_type, text_search, voice_search, image_search, clothes_fields)
        if product_type == 'mobile':
            result = self.search_mobile(search_type, text_search, voice_search, image_search, mobile_fields)

        response_data = {
            'products': result,
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
    
    def search_product(self, search_type, text_search, voice_search, image_search):
        api_url = 'http://localhost:8002/product/all/'
        response = requests.get(api_url)
        products = response.json() 
        result = []           
        
        if search_type == 'text' or search_type == 'voice':
            if search_type == 'text':
                search_data = text_search
            else:
                search_data = voice_search
                
            search_data = search_data.lower()
            for product in products:
                name = product['name']
                if search_data in name.lower():
                    result.append(product)
        else:
            # get_image_features_list(True)
            # result = products
            
            similar_product_ids = predict_similar_image(image_search)
            for product in products:
                id = product['id']
                if id in similar_product_ids:
                    result.append(product)
        
        return result
    
    
    def search_book(self, search_type, text_search, voice_search, image_search, book_fields):
        api_url = 'http://localhost:8002/book/all/'
        response = requests.get(api_url)
        books = response.json() 
        result = []
        
        if search_type == 'text' or search_type == 'voice':
            if search_type == 'text':
                search_data = text_search
            else:
                search_data = voice_search
                
            search_data = search_data.lower()
            if book_fields == 'name':
                for book in books:
                    if search_data in book['product']['name'].lower():
                        result.append(book['product'])
            
            elif book_fields == 'author':
                for book in books:
                    if search_data in book['author']['name'].lower():
                        result.append(book['product'])
                        
            elif book_fields == 'genre':
                for book in books:
                    for genre in book['genres']:
                        if search_data in genre['name'].lower():
                            result.append(book['product'])
                            break
        
        else:
            # result = [book['product'] for book in books]
            similar_product_ids = predict_similar_image(image_search)
            for book in books:
                id = book['product']['id']
                if id in similar_product_ids:
                    result.append(book['product'])
        
        return result
    
    
    def search_clothes(self, search_type, text_search, voice_search, image_search, clothes_fields):
        api_url = 'http://localhost:8002/clothes/all/'
        response = requests.get(api_url)
        clothes = response.json() 
        result = []
        
        if search_type == 'text' or search_type == 'voice':
            if search_type == 'text':
                search_data = text_search
            else:
                search_data = voice_search
                
            search_data = search_data.lower()
            if clothes_fields == 'name':
                for clothing_item in clothes:
                    if search_data in clothing_item['product']['name'].lower():
                        result.append(clothing_item['product'])
            
            elif clothes_fields == 'manufacturer':
                for clothing_item in clothes:
                    if search_data in clothing_item['manufacturer']['name'].lower():
                        result.append(clothing_item['product'])
                        
            elif clothes_fields == 'style':
                for clothing_item in clothes:
                    for style in clothing_item['styles']:
                        if search_data in style['name'].lower():
                            result.append(clothing_item['product'])
                            break
        
        else:
            # result = [clothing_item['product'] for clothing_item in clothes]
            similar_product_ids = predict_similar_image(image_search)
            for clothe in clothes:
                id = clothe['product']['id']
                if id in similar_product_ids:
                    result.append(clothe['product'])
        
        return result
    
    
    def search_mobile(self, search_type, text_search, voice_search, image_search, mobile_fields):
        api_url = 'http://localhost:8002/mobile/all/'
        response = requests.get(api_url)
        mobiles = response.json() 
        result = []
        
        if search_type == 'text' or search_type == 'voice':
            if search_type == 'text':
                search_data = text_search
            else:
                search_data = voice_search
                
            search_data = search_data.lower()
            if mobile_fields == 'name':
                for mobile in mobiles:
                    if search_data in mobile['product']['name'].lower():
                        result.append(mobile['product'])
            
            elif mobile_fields == 'manufacturer':
                for mobile in mobiles:
                    if search_data in mobile['manufacturer']['name'].lower():
                        result.append(mobile['product'])
                        
            elif mobile_fields == 'mobile_type':
                for mobile in mobiles:
                    if search_data in mobile['mobile_type']['name'].lower():
                        result.append(mobile['product'])
        
        else:
            # result = [mobile['product'] for mobile in mobiles]
            similar_product_ids = predict_similar_image(image_search)
            for mobile in mobiles:
                id = mobile['product']['id']
                if id in similar_product_ids:
                    result.append(mobile['product'])
        
        return result