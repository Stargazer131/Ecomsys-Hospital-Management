from django.urls import path
from healthcare import views


urlpatterns = [
    # Doctor URLs
    path('doctor/all/', views.DoctorListAPIView.as_view(), name='doctor-list'),
    path('doctor/get/<int:pk>/', views.DoctorRetrieveAPIView.as_view(), name='doctor-detail'),
    path('doctor/create/', views.DoctorCreateAPIView.as_view(), name='doctor-create'),
    path('doctor/update/<int:pk>/', views.DoctorUpdateAPIView.as_view(), name='doctor-update'),
    path('doctor/delete/<int:pk>/', views.DoctorDestroyAPIView.as_view(), name='doctor-delete'),

    # Nurse URLs
    path('nurse/all/', views.NurseListAPIView.as_view(), name='nurse-list'),
    path('nurse/get/<int:pk>/', views.NurseRetrieveAPIView.as_view(), name='nurse-detail'),
    path('nurse/create/', views.NurseCreateAPIView.as_view(), name='nurse-create'),
    path('nurse/update/<int:pk>/', views.NurseUpdateAPIView.as_view(), name='nurse-update'),
    path('nurse/delete/<int:pk>/', views.NurseDestroyAPIView.as_view(), name='nurse-delete'),

    # Pharmacist URLs
    path('pharmacist/all/', views.PharmacistListAPIView.as_view(), name='pharmacist-list'),
    path('pharmacist/get/<int:pk>/', views.PharmacistRetrieveAPIView.as_view(), name='pharmacist-detail'),
    path('pharmacist/create/', views.PharmacistCreateAPIView.as_view(), name='pharmacist-create'),
    path('pharmacist/update/<int:pk>/', views.PharmacistUpdateAPIView.as_view(), name='pharmacist-update'),
    path('pharmacist/delete/<int:pk>/', views.PharmacistDestroyAPIView.as_view(), name='pharmacist-delete'),

    # LabTechnician URLs
    path('labtechnician/all/', views.LabTechnicianListAPIView.as_view(), name='labtechnician-list'),
    path('labtechnician/get/<int:pk>/', views.LabTechnicianRetrieveAPIView.as_view(), name='labtechnician-detail'),
    path('labtechnician/create/', views.LabTechnicianCreateAPIView.as_view(), name='labtechnician-create'),
    path('labtechnician/update/<int:pk>/', views.LabTechnicianUpdateAPIView.as_view(), name='labtechnician-update'),
    path('labtechnician/delete/<int:pk>/', views.LabTechnicianDestroyAPIView.as_view(), name='labtechnician-delete'),
]
