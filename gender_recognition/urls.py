from django.urls import path
from gender_recognition.views import predict_gender

urlpatterns = [
    path("predict_gender", predict_gender, name="predict_gender")
]
