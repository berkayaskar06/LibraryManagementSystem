from django.contrib import admin
from .models import Books
# Register your models here.

class postAdmin(admin.ModelAdmin):

    list_display = ['title','author']
    list_display_links = ['title','author']
    list_filter = ['flag']
    search_fields = ['title','author']

    class Meta:
        model = Books





admin.site.register(Books,postAdmin)
