import json
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import JsonResponse
from .utilities import TranslateNumber


# Hit this endpoint with POST: /api/num_to_english
# Hit this endpoint with GET: /api/num_to_english?number=12345678
# See ../bash_scripts to see how to hit this endpoint using "curl"
class NumToEnglish(APIView):
    def get(self, request):
        number = request.GET.get("number", "")
        validation = self.validate(number)
        print(validation)
        if validation[0] == False:
            return validation[1]
        number = int(number)
        english_number = TranslateNumber(number).to_english()
        data = {"status": "ok", "num_in_english": english_number}
        return JsonResponse(
            data, status=status.HTTP_200_OK, json_dumps_params={"indent": 2}
        )

    def post(self, request):
        number = json.loads(request.body)
        number = number.get("number", "")
        validation = self.validate(number)
        if validation[0] == False:
            return validation[1]
        number = int(number)
        english_number = TranslateNumber(number).to_english()
        data = {"status": "ok", "english_number": english_number}
        return JsonResponse(
            data, status=status.HTTP_200_OK, json_dumps_params={"indent": 2}
        )

    # Validation code for Post and Get
    def validate(self, number):
        if number:
            try:
                number = int(number)
            except:
                data = {
                    "status": "Bad Request",
                    "error": "Could not convert input to an integer.",
                }
                return (
                    False,
                    JsonResponse(
                        data,
                        status=status.HTTP_400_BAD_REQUEST,
                        json_dumps_params={"indent": 2},
                    ),
                )
        else:
            data = {"status": "Bad Request", "error": "Not a valid number..."}
            return (
                False,
                JsonResponse(
                    data,
                    status=status.HTTP_400_BAD_REQUEST,
                    json_dumps_params={"indent": 2},
                ),
            )
        if len(str(number)) > 9:
            data = {
                "status": "Bad Request",
                "error": "Only numbers of length 9 or less are allowed.",
            }
            return (
                False,
                JsonResponse(
                    data,
                    status=status.HTTP_400_BAD_REQUEST,
                    json_dumps_params={"indent": 2},
                ),
            )
        return (True, None)
