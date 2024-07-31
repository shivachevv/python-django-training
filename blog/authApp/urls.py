from django.urls import path
from . import views

app_name = 'authApp'

urlpatterns = [
    path('login/', views.login_controller, name='login'),
    path('register/', views.register_controller, name='register'),
    path('logout/', views.logout_controller, name="logout"),
]
