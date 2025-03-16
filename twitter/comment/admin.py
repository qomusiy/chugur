from django.contrib import admin
from .models import Comment
# Register your models here.

class ComTab(admin.ModelAdmin):
    list_display = ('writer', 'sent_date', 'itself')
    search_fields = ('writer', 'itself')

admin.site.register(Comment, ComTab)