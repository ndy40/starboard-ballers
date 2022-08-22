from django.template import Library
from game_sessions.models import Session

register = Library()


@register.inclusion_tag('game_sessions/_partial_join_button.html')
def show_session_join_button(session: Session, user):
    user = session.players.filter(session__players__pk=user.pk)

    return {'show': 'leave' if user else 'join', 'session': session }
