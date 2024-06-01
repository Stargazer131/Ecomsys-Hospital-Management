from django.urls import path
from product import views


urlpatterns = [    
    path('all/', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductRetrieveView.as_view(), name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.ProductDestroyView.as_view(), name='product_delete'),
]

