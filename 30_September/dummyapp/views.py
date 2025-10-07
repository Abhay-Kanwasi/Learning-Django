from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def testing(request):
    print(request)
    return JsonResponse({'status': 'success'})

# 127.0.0.1:8000/dummy/testing/