from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['user', 'page_name', 'page_publish_date']

admin.site.register(Page, PageAdmin)