from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_confirmation, name='account_logout'),
    path('profile/', views.profile_view, name='profile'),
]
