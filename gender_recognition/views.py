from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from gender_recognition.genderPredictor import genderPredict


def predict_gender(request):
    try:
        if "name" in request.GET:
            name = request.GET["name"]
            result = genderPredict(name)
            return JsonResponse({"Gender": result})
        else:
            return HttpResponseBadRequest("Missing Parameter")
    except Exception:
        return JsonResponse({"message": "Server Error"}, status=500)
