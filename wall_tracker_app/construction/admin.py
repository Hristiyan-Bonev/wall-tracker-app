from django.contrib import admin
from .models import WallProfile, Section

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1

@admin.register(WallProfile)
class WallProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [SectionInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'initial_height', 'current_height', 'completed_day')
    list_filter = ('profile',)