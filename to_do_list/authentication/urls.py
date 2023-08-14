from django.urls import path
from .views import LoginPage, RegisterPage, LogoutPage,PasswordsChangeView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[

    # urls login logout and register page
    path('login/', LoginPage.as_view(), name='user_login'),

    path('logout/',LogoutPage.as_view(), name= 'logout'),

    path('register/', RegisterPage.as_view(), name='user_registration'),
    
    path('dashboard', views.Dashboard, name='dashboard' ),

    # path('change-password/<token>/', views.ChangePassword, name='change-password'),

    # path('forgot-password/', views.forgetPassword, name='forgot-password'),


    # path('password/',auth_views.PasswordChangeView.as_view(template_name='authentication/change-password.html' )),
    path('change-password/', PasswordsChangeView.as_view(template_name='authentication/change-password.html'),name='change-password'),
]
