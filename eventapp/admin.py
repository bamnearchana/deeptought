from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('type','uid','name','tagline','schedule','description',
                    'files','moderator','category','sub_category','rigor_rank','attendees')
