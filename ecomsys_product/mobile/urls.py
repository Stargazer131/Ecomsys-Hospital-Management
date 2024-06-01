from django.urls import path
from mobile import views

urlpatterns = [
    path('all/', views.MobileListView.as_view(), name='mobile_list'),
    path('<int:pk>/', views.MobileRetrieveView.as_view(), name='mobile_detail'),
    path('create/', views.MobileCreateView.as_view(), name='mobile_create'),
    path('<int:pk>/update/', views.MobileUpdateView.as_view(), name='mobile_update'),
    path('<int:pk>/delete/', views.MobileDestroyView.as_view(), name='mobile_delete'),
]

