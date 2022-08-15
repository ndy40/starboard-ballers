from django.shortcuts import render

# Create your views here.


def list_sessions(request):
    return render(request, 'game_sessions/sessions.html', {})
