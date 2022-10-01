from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators import http

# Create your views here.


@http.require_http_methods(['GET'])
def frontend_app(request):
    social = request.user.social_auth.get(provider='starballers')
    token = social.extra_data.get('access_token')
    return render(request, 'frontend.html', {'access_token': token})

