from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)