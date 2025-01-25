from django.contrib import admin
from .models import AboutUs
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AboutUs)
class AboutAdmin(admin.ModelAdmin):
    
   list_display = ('title', 'description','added_on')
   search_fields = ['title']
    
#admin.site.register(AboutUs)