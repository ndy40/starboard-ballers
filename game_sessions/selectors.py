from datetime import datetime

from .models import Session


def get_upcoming_sessions():
    return Session.objects.filter(session_date__gte=datetime.utcnow())
