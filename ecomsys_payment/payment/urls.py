from django.urls import path
from payment import views


urlpatterns = [
    path('method/all/', views.PaymentMethodListAPIView.as_view(), name='payment_method_list'),
    path('all/', views.PaymentListView.as_view(), name='payment_list'),
    path('<int:pk>/', views.PaymentRetrieveView.as_view(), name='payment_detail'),
    path('create/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('<int:pk>/update/', views.PaymentUpdateView.as_view(), name='payment_update'),
    path('<int:pk>/delete/', views.PaymentDestroyView.as_view(), name='payment_delete'),
]