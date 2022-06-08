from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):
    # request->HttpResponse-> Django
    # print(request.GET)
    body = request.body # JSON data
    data = {}
    try:
        data = json.loads(body)     # string of JSON data -> Python Dict
    except:
        pass
    # print(data.keys())
    # print(body)
    # print(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    data['headers'] = (dict(request.headers))
    # print(data)
    # return JsonResponse({"message":"Hi there, this is your Django API response! "})
    return JsonResponse(data)