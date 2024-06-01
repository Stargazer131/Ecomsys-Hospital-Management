from django.urls import path
from . import views


urlpatterns = [
    # Building URLs
    path('building/all/', views.BuildingListAPIView.as_view(), name='building-list'),
    path('building/get/<int:pk>/', views.BuildingRetrieveAPIView.as_view(), name='building-detail'),
    path('building/create/', views.BuildingCreateAPIView.as_view(), name='building-create'),
    path('building/update/<int:pk>/', views.BuildingUpdateAPIView.as_view(), name='building-update'),
    path('building/delete/<int:pk>/', views.BuildingDestroyAPIView.as_view(), name='building-delete'),

    # Room URLs
    path('room/all/', views.RoomListAPIView.as_view(), name='room-list'),
    path('room/get/<int:pk>/', views.RoomRetrieveAPIView.as_view(), name='room-detail'),
    path('room/create/', views.RoomCreateAPIView.as_view(), name='room-create'),
    path('room/update/<int:pk>/', views.RoomUpdateAPIView.as_view(), name='room-update'),
    path('room/delete/<int:pk>/', views.RoomDestroyAPIView.as_view(), name='room-delete'),

    # Bed URLs
    path('bed/all/', views.BedListAPIView.as_view(), name='bed-list'),
    path('bed/get/<int:pk>/', views.BedRetrieveAPIView.as_view(), name='bed-detail'),
    path('bed/create/', views.BedCreateAPIView.as_view(), name='bed-create'),
    path('bed/update/<int:pk>/', views.BedUpdateAPIView.as_view(), name='bed-update'),
    path('bed/delete/<int:pk>/', views.BedDestroyAPIView.as_view(), name='bed-delete'),

    # Furniture URLs
    path('furniture/all/', views.FurnitureListAPIView.as_view(), name='furniture-list'),
    path('furniture/get/<int:pk>/', views.FurnitureRetrieveAPIView.as_view(), name='furniture-detail'),
    path('furniture/create/', views.FurnitureCreateAPIView.as_view(), name='furniture-create'),
    path('furniture/update/<int:pk>/', views.FurnitureUpdateAPIView.as_view(), name='furniture-update'),
    path('furniture/delete/<int:pk>/', views.FurnitureDestroyAPIView.as_view(), name='furniture-delete'),

    # MedicalEquipment URLs
    path('medicalequipment/all/', views.MedicalEquipmentListAPIView.as_view(), name='medicalequipment-list'),
    path('medicalequipment/get/<int:pk>/', views.MedicalEquipmentRetrieveAPIView.as_view(), name='medicalequipment-detail'),
    path('medicalequipment/create/', views.MedicalEquipmentCreateAPIView.as_view(), name='medicalequipment-create'),
    path('medicalequipment/update/<int:pk>/', views.MedicalEquipmentUpdateAPIView.as_view(), name='medicalequipment-update'),
    path('medicalequipment/delete/<int:pk>/', views.MedicalEquipmentDestroyAPIView.as_view(), name='medicalequipment-delete'),
]
