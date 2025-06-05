from django.contrib import admin
from .models import JournalLevel

@admin.register(JournalLevel)
class JournalLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)
