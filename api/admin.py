from django.contrib import admin
from .models import Group, Faculty, Theme, Practise

admin.site.register(Group)
admin.site.register(Faculty)
admin.site.register(Theme)

@admin.register(Practise)
class PractiseAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'theme', 'group', 'author', 'camera_pdf', 'pdf', 'created', 'updated', 'is_valid')
    list_filter = ['faculty',  'group', 'is_valid']
    search_fields = ['author']