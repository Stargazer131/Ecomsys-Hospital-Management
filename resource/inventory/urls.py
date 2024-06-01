from django.urls import path
from . import views


urlpatterns = [
    # Manufacturer URLs
    path('manufacturer/all/', views.ManufacturerListAPIView.as_view(), name='manufacturer-list'),
    path('manufacturer/get/<int:pk>/', views.ManufacturerRetrieveAPIView.as_view(), name='manufacturer-detail'),
    path('manufacturer/create/', views.ManufacturerCreateAPIView.as_view(), name='manufacturer-create'),
    path('manufacturer/update/<int:pk>/', views.ManufacturerUpdateAPIView.as_view(), name='manufacturer-update'),
    path('manufacturer/delete/<int:pk>/', views.ManufacturerDestroyAPIView.as_view(), name='manufacturer-delete'),

    # Resource URLs
    path('resource/all/', views.ResourceListAPIView.as_view(), name='resource-list'),
    path('resource/get/<int:pk>/', views.ResourceRetrieveAPIView.as_view(), name='resource-detail'),
    path('resource/create/', views.ResourceCreateAPIView.as_view(), name='resource-create'),
    path('resource/update/<int:pk>/', views.ResourceUpdateAPIView.as_view(), name='resource-update'),
    path('resource/delete/<int:pk>/', views.ResourceDestroyAPIView.as_view(), name='resource-delete'),

    # Bill URLs
    path('bill/all/', views.BillListAPIView.as_view(), name='bill-list'),
    path('bill/get/<int:pk>/', views.BillRetrieveAPIView.as_view(), name='bill-detail'),
    path('bill/create/', views.BillCreateAPIView.as_view(), name='bill-create'),
    path('bill/update/<int:pk>/', views.BillUpdateAPIView.as_view(), name='bill-update'),
    path('bill/delete/<int:pk>/', views.BillDestroyAPIView.as_view(), name='bill-delete'),

    # Medication URLs
    path('medication/all/', views.MedicationListAPIView.as_view(), name='medication-list'),
    path('medication/get/<int:pk>/', views.MedicationRetrieveAPIView.as_view(), name='medication-detail'),
    path('medication/create/', views.MedicationCreateAPIView.as_view(), name='medication-create'),
    path('medication/update/<int:pk>/', views.MedicationUpdateAPIView.as_view(), name='medication-update'),
    path('medication/delete/<int:pk>/', views.MedicationDestroyAPIView.as_view(), name='medication-delete'),

    # Supply URLs
    path('supply/all/', views.SupplyListAPIView.as_view(), name='supply-list'),
    path('supply/get/<int:pk>/', views.SupplyRetrieveAPIView.as_view(), name='supply-detail'),
    path('supply/create/', views.SupplyCreateAPIView.as_view(), name='supply-create'),
    path('supply/update/<int:pk>/', views.SupplyUpdateAPIView.as_view(), name='supply-update'),
    path('supply/delete/<int:pk>/', views.SupplyDestroyAPIView.as_view(), name='supply-delete'),

    # BillItem URLs
    path('billitem/all/', views.BillItemListAPIView.as_view(), name='billitem-list'),
    path('billitem/get/<int:pk>/', views.BillItemRetrieveAPIView.as_view(), name='billitem-detail'),
    path('billitem/create/', views.BillItemCreateAPIView.as_view(), name='billitem-create'),
    path('billitem/update/<int:pk>/', views.BillItemUpdateAPIView.as_view(), name='billitem-update'),
    path('billitem/delete/<int:pk>/', views.BillItemDestroyAPIView.as_view(), name='billitem-delete'),
]
