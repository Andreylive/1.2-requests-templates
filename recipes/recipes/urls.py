from django.urls import path
from calculator.views import recipes_views

urlpatterns = [
    path('<dish_name>/', recipes_views),
]