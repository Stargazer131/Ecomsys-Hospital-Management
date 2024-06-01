from django.urls import path
from . import views


urlpatterns = [
    # Invoice URLs
    path('invoice/all/', views.InvoiceListAPIView.as_view(), name='invoice-list'),
    path('invoice/get/<int:pk>/', views.InvoiceRetrieveAPIView.as_view(), name='invoice-detail'),
    path('invoice/create/', views.InvoiceCreateAPIView.as_view(), name='invoice-create'),
    path('invoice/update/<int:pk>/', views.InvoiceUpdateAPIView.as_view(), name='invoice-update'),
    path('invoice/delete/<int:pk>/', views.InvoiceDestroyAPIView.as_view(), name='invoice-delete'),

    # Payment URLs
    path('payment/all/', views.PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/get/<int:pk>/', views.PaymentRetrieveAPIView.as_view(), name='payment-detail'),
    path('payment/create/', views.PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/update/<int:pk>/', views.PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:pk>/', views.PaymentDestroyAPIView.as_view(), name='payment-delete'),
]
