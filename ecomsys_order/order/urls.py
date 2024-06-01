from django.urls import path
from order import views


urlpatterns = [
    path('create/', views.PlaceOrderAPIView.as_view(), name='place_order'),
    path('all/', views.OrderListView.as_view(), name='order_list'),
    path('<int:pk>/', views.OrderRetrieveView.as_view(), name='order_detail'),
    path('<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('<int:pk>/delete/', views.OrderDestroyView.as_view(), name='order_delete'),
]