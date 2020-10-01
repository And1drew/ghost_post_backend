from django.urls import path
from boastOrRoast import views

urlpatterns = [
    path('', views.index)
]
