from django.urls import path
from customer import views


urlpatterns = [    
    path('login/', views.CustomerLoginAPIView.as_view(), name='customer_login'),
    path('register/', views.CustomerRegisterAPIView.as_view(), name='customer_register'),
    path('all/', views.CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/', views.CustomerRetrieveView.as_view(), name='customer_detail'),
    path('create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('<int:pk>/delete/', views.CustomerDestroyView.as_view(), name='customer_delete'),
]

