from django.urls import path
from product import views


urlpatterns = [
    path('all/', views.ProductListView.as_view(), name='product_list'),
]

