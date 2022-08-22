from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.list_sessions, name='sessions'),
    path('<int:session_id>/join', views.join_session, name='join_session'),
    path('<int:session_id>/leave', views.leave_session, name='leave_session')
]
