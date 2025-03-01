from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # Route for homepage
    path('predict/', views.predict_price, name='predict'),  # Route for predictions
]


