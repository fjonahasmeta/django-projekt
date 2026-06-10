from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('post/<int:pk>/', views.post_detail, name='detail'),

    path('create/', views.create_post, name='create'),
    path('edit/<int:pk>/', views.edit_post, name='edit'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),

    path('booking/<int:pk>/', views.booking, name='booking'),

    path('like/<int:pk>/', views.like_post, name='like'),
    path('dislike/<int:pk>/', views.dislike_post, name='dislike'),
]