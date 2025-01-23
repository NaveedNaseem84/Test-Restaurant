from django.contrib import admin
from .models import MenuItem
from django_summernote.admin import SummernoteModelAdmin

@admin.register(MenuItem)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('name', 'description','price', 'category')
    search_fields = ['name','category']
    list_filter = ('name','category')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)


# Register your models here.
#admin.site.register(MenuItem)
