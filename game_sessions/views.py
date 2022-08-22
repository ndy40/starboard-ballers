from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Session, Player
from . import selectors


# Create your views here.

@login_required
def list_sessions(request):
    sessions = selectors.get_upcoming_sessions()
    return render(request, 'game_sessions/sessions.html', {'sessions': sessions})


@login_required
def join_session(request, session_id):
    print(request.user.id)
    user = get_object_or_404(Player, pk=request.user.id)
    session = get_object_or_404(Session, pk=session_id)
    session.players.add(user)
    session.save()

    return redirect('/sessions')


@login_required
def leave_session(request, session_id):
    user = get_object_or_404(Player, pk=request.user.id)
    session = get_object_or_404(Session, pk=session_id)
    session.players.remove(user)

    return redirect('/sessions')
