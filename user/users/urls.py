from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('user/all/', views.UserListAPIView.as_view(), name='user-list'),
    path('user/get/<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user-detail'),
    path('user/create/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('user/update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', views.UserDestroyAPIView.as_view(), name='user-delete'),

    # Account URLs
    path('account/all/', views.AccountListAPIView.as_view(), name='account-list'),
    path('account/get/<int:pk>/', views.AccountRetrieveAPIView.as_view(), name='account-detail'),
    path('account/create/', views.AccountCreateAPIView.as_view(), name='account-create'),
    path('account/update/<int:pk>/', views.AccountUpdateAPIView.as_view(), name='account-update'),
    path('account/delete/<int:pk>/', views.AccountDestroyAPIView.as_view(), name='account-delete'),
    
    # Fullname URLs
    path('fullname/all/', views.FullnameListAPIView.as_view(), name='fullname-list'),
    path('fullname/get/<int:pk>/', views.FullnameRetrieveAPIView.as_view(), name='fullname-detail'),
    path('fullname/create/', views.FullnameCreateAPIView.as_view(), name='fullname-create'),
    path('fullname/update/<int:pk>/', views.FullnameUpdateAPIView.as_view(), name='fullname-update'),
    path('fullname/delete/<int:pk>/', views.FullnameDestroyAPIView.as_view(), name='fullname-delete'),
]
