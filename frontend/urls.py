from django.urls import path
from .views import index

urlpatterns = [
    path("num_translator", index, name=""),
    path("", index, name=""),
]
