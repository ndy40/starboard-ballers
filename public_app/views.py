from django.shortcuts import render

# Create your views here.


def frontend_app(request):
    return render(request, 'frontend.html')
