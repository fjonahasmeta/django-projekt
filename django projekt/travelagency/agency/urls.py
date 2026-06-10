from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 🏠 HOME
    path('', views.home, name='home'),

    # 📄 DETAIL
    path('post/<int:pk>/', views.post_detail, name='detail'),

    # ➕ CRUD POSTS
    path('create/', views.create_post, name='create'),
    path('edit/<int:pk>/', views.edit_post, name='edit'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),

    # 📅 BOOKING
    path('booking/<int:pk>/', views.booking, name='booking'),

    # ❤️ LIKE / DISLIKE
    path('like/<int:pk>/', views.like_post, name='like'),
    path('dislike/<int:pk>/', views.dislike_post, name='dislike'),

    # 📄 STATIC PAGES
    path('about/', views.about, name='about'),
    path('help/', views.help_page, name='help'),

    # 🔐 AUTH
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]