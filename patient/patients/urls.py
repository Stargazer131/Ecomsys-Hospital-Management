from django.urls import path
from patients import views


urlpatterns = [
    # Patient URLs
    path('patient/all/', views.PatientListAPIView.as_view(), name='patient-list'),
    path('patient/get/<int:pk>/', views.PatientRetrieveAPIView.as_view(), name='patient-detail'),
    path('patient/create/', views.PatientCreateAPIView.as_view(), name='patient-create'),
    path('patient/update/<int:pk>/', views.PatientUpdateAPIView.as_view(), name='patient-update'),
    path('patient/delete/<int:pk>/', views.PatientDestroyAPIView.as_view(), name='patient-delete'),

    # MedicalRecord URLs
    path('medicalrecord/all/', views.MedicalRecordListAPIView.as_view(), name='medicalrecord-list'),
    path('medicalrecord/get/<int:pk>/', views.MedicalRecordRetrieveAPIView.as_view(), name='medicalrecord-detail'),
    path('medicalrecord/create/', views.MedicalRecordCreateAPIView.as_view(), name='medicalrecord-create'),
    path('medicalrecord/update/<int:pk>/', views.MedicalRecordUpdateAPIView.as_view(), name='medicalrecord-update'),
    path('medicalrecord/delete/<int:pk>/', views.MedicalRecordDestroyAPIView.as_view(), name='medicalrecord-delete'),

    # LabTest URLs
    path('labtest/all/', views.LabTestListAPIView.as_view(), name='labtest-list'),
    path('labtest/get/<int:pk>/', views.LabTestRetrieveAPIView.as_view(), name='labtest-detail'),
    path('labtest/create/', views.LabTestCreateAPIView.as_view(), name='labtest-create'),
    path('labtest/update/<int:pk>/', views.LabTestUpdateAPIView.as_view(), name='labtest-update'),
    path('labtest/delete/<int:pk>/', views.LabTestDestroyAPIView.as_view(), name='labtest-delete'),

    # Prescription URLs
    path('prescription/all/', views.PrescriptionListAPIView.as_view(), name='prescription-list'),
    path('prescription/get/<int:pk>/', views.PrescriptionRetrieveAPIView.as_view(), name='prescription-detail'),
    path('prescription/create/', views.PrescriptionCreateAPIView.as_view(), name='prescription-create'),
    path('prescription/update/<int:pk>/', views.PrescriptionUpdateAPIView.as_view(), name='prescription-update'),
    path('prescription/delete/<int:pk>/', views.PrescriptionDestroyAPIView.as_view(), name='prescription-delete'),

    # Treatment URLs
    path('treatment/all/', views.TreatmentListAPIView.as_view(), name='treatment-list'),
    path('treatment/get/<int:pk>/', views.TreatmentRetrieveAPIView.as_view(), name='treatment-detail'),
    path('treatment/create/', views.TreatmentCreateAPIView.as_view(), name='treatment-create'),
    path('treatment/update/<int:pk>/', views.TreatmentUpdateAPIView.as_view(), name='treatment-update'),
    path('treatment/delete/<int:pk>/', views.TreatmentDestroyAPIView.as_view(), name='treatment-delete'),
]
