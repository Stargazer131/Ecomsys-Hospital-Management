from django.urls import path
from clothes import views


urlpatterns = [
    path('all/', views.ClothingItemListView.as_view(), name='clothing_item_list'),
    path('<int:pk>/', views.ClothingItemRetrieveView.as_view(), name='clothing_item_detail'),
    path('create/', views.ClothingItemCreateView.as_view(), name='clothing_item_create'),
    path('<int:pk>/update/', views.ClothingItemUpdateView.as_view(), name='clothing_item_update'),
    path('<int:pk>/delete/', views.ClothingItemDestroyView.as_view(), name='clothing_item_delete'),
]

