from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('gender_recognition/', include('gender_recognition.urls'))
]
