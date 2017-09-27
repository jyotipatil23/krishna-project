from django.http import HttpResponse, JsonResponse
from django.shorcuts import render
import json


def Krishna_project(request):
    # get data from request
    jsonObj = json.loads(request.body)

    # assign input data to respective variables
    Name = jsonObj.get("Name")
    Email_ID = jsonObj.get("Email_ID")
    phone_no = jsonObj.get("phone_no")
    country_name = jsonObj.get("country_name")
    message = jsonObj.get("message")

    if not Name:
            return JsonResponse({"validation": "Enter name", "status": False})
    if not Email_ID:
            return JsonResponse({"validation": "Enter Email_id", "status": False})
    if not phone_no:
            return JsonResponse({"validation": "Enter phone No.", "status": False})
    if not country_name:
            return JsonResponse({"validation": "Enter your country", "status": False})
    

    # create truck object
    krishna_project = Krishna_project.objects.create(Name=Name,
                                     Email_ID=Email_ID,
                                     phone_no=phone_no,
                                     country_name=country_name,
                                     message=message
                                     )

    # truck = TruckInfo.objects.create(**jsonObj)

    # Return response
    return JsonResponse({"validation": "New user created", "status": True})