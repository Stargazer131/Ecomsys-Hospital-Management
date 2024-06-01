from django.urls import path
from cart import views


urlpatterns = [
    path('', views.ShowCartView.as_view(), name='show_cart'),
]

