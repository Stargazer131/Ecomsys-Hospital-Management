from django.urls import path
from search import views


urlpatterns = [
    path('', views.SearchByNameView.as_view(), name='search'),
]

