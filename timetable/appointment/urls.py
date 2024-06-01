from django.urls import path
from appointment import views


urlpatterns = [
    # Appointment URLs
    path('appointment/all/', views.AppointmentListAPIView.as_view(), name='appointment-list'),
    path('appointment/get/<int:pk>/', views.AppointmentRetrieveAPIView.as_view(), name='appointment-detail'),
    path('appointment/create/', views.AppointmentCreateAPIView.as_view(), name='appointment-create'),
    path('appointment/update/<int:pk>/', views.AppointmentUpdateAPIView.as_view(), name='appointment-update'),
    path('appointment/delete/<int:pk>/', views.AppointmentDestroyAPIView.as_view(), name='appointment-delete'),
]
