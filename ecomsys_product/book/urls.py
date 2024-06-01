from django.urls import path
from book import views


urlpatterns = [
    path('all/', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookRetrieveView.as_view(), name='book_detail'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDestroyView.as_view(), name='book_delete'),
]

