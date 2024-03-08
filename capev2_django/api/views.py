from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseServerError
import requests

# Create your views here.
def analyze_file(request, *args, **kwargs):
    url = 'https://capesandbox.com/apiv2/analyze_file'  # Example API endpoint URL
    headers = {'Authorization': 'Token d629af8a5ea6f92294d887019e7fccca554bb109'}

    if request.method == 'POST':
        file = request.FILES['file']
        files = {'file': file}
        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            # Handle successful response
            data = response.json()
            return JsonResponse(data)
        else:
            # Handle error response
            return HttpResponseServerError("Failed to analyze file")
