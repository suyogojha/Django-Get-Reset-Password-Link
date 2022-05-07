from django.urls import path
from home import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
