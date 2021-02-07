from django.urls import path
from .views import NumToEnglish

urlpatterns = [
    path("num_to_english", NumToEnglish.as_view()),
]
