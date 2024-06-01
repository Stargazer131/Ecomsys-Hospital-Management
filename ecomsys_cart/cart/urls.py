from django.urls import path
from cart import views


urlpatterns = [
    path('', views.CartListAPIView.as_view(), name='cart_list'),
    path('cart-item/update/', views.CartItemAPIView.as_view(), name='cart_item_update'),
]

