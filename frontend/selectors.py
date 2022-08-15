from game_sessions.models import Player


def authenticate(email: str):
    try:
        return Player.objects.get(email=email)
    except Player.DoesNotExist:
        pass

