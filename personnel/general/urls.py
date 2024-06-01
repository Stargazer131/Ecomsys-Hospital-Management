from django.urls import path
from general import views


urlpatterns = [
    # Staff URLs
    path('staff/all/', views.StaffListAPIView.as_view(), name='staff-list'),
    path('staff/get/<int:pk>/', views.StaffRetrieveAPIView.as_view(), name='staff-detail'),
    path('staff/create/', views.StaffCreateAPIView.as_view(), name='staff-create'),
    path('staff/update/<int:pk>/', views.StaffUpdateAPIView.as_view(), name='staff-update'),
    path('staff/delete/<int:pk>/', views.StaffDestroyAPIView.as_view(), name='staff-delete'),

    # Manager URLs
    path('manager/all/', views.ManagerListAPIView.as_view(), name='manager-list'),
    path('manager/get/<int:pk>/', views.ManagerRetrieveAPIView.as_view(), name='manager-detail'),
    path('manager/create/', views.ManagerCreateAPIView.as_view(), name='manager-create'),
    path('manager/update/<int:pk>/', views.ManagerUpdateAPIView.as_view(), name='manager-update'),
    path('manager/delete/<int:pk>/', views.ManagerDestroyAPIView.as_view(), name='manager-delete'),

    # Receptionist URLs
    path('receptionist/all/', views.ReceptionistListAPIView.as_view(), name='receptionist-list'),
    path('receptionist/get/<int:pk>/', views.ReceptionistRetrieveAPIView.as_view(), name='receptionist-detail'),
    path('receptionist/create/', views.ReceptionistCreateAPIView.as_view(), name='receptionist-create'),
    path('receptionist/update/<int:pk>/', views.ReceptionistUpdateAPIView.as_view(), name='receptionist-update'),
    path('receptionist/delete/<int:pk>/', views.ReceptionistDestroyAPIView.as_view(), name='receptionist-delete'),
]
