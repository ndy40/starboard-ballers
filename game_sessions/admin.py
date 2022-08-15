from datetime import datetime
from django.contrib import admin

from .models import Session, Venue, Player

# Register your models here.


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def get_queryset(self, request):
        return Player.players


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    verbose_name = 'Game Session Manager'
    exclude = ['created_by']
    list_display = ['session_date', 'venue', 'max_players', 'cost', 'number_of_players', 'created_by']
    list_filter = ['session_date', 'venue']
    sortable_by = ['session_date', 'max_players']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(SessionAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(created_by=request.user, session_date__gte=datetime.now())




