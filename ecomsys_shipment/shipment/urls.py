from django.urls import path
from shipment import views


urlpatterns = [
    path('method/all/', views.ShipmentMethodListAPIView.as_view(), name='shipment_method_list'),
    path('all/', views.ShipmentListView.as_view(), name='shipment_list'),
    path('<int:pk>/', views.ShipmentRetrieveView.as_view(), name='shipment_detail'),
    path('create/', views.ShipmentCreateView.as_view(), name='shipment_create'),
    path('<int:pk>/update/', views.ShipmentUpdateView.as_view(), name='shipment_update'),
    path('<int:pk>/delete/', views.ShipmentDestroyView.as_view(), name='shipment_delete'),
]