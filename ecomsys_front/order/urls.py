from django.urls import path
from order import views


urlpatterns = [
    path('', views.PlaceOrderView.as_view(), name='place_order'),
]