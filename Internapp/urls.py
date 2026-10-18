from django.urls import path, include
from .import views

# Import the views file from the current directory

urlpatterns = [
    path('', views.home, name='index.html'),
    path('db/', views.db_view, name='db.html'),
]