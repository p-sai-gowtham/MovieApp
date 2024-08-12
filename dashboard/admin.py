from django.contrib import admin
from .models import theatre_manager, theatre, screen, movie, show

# Register your models here.
admin.site.register(theatre_manager)
admin.site.register(theatre)
admin.site.register(screen)
admin.site.register(movie)
admin.site.register(show)
