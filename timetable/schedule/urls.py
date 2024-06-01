from django.urls import path
from . import views


urlpatterns = [
    # Schedule URLs
    path('schedule/all/', views.ScheduleListAPIView.as_view(), name='schedule-list'),
    path('schedule/get/<int:pk>/', views.ScheduleRetrieveAPIView.as_view(), name='schedule-detail'),
    path('schedule/create/', views.ScheduleCreateAPIView.as_view(), name='schedule-create'),
    path('schedule/update/<int:pk>/', views.ScheduleUpdateAPIView.as_view(), name='schedule-update'),
    path('schedule/delete/<int:pk>/', views.ScheduleDestroyAPIView.as_view(), name='schedule-delete'),
]
