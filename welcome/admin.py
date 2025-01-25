from django.contrib import admin
from .models import WelcomeInfo
from django_summernote.admin import SummernoteModelAdmin

@admin.register(WelcomeInfo)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('welcome_title', 'description','contact_info')
    search_fields = ['welcome_title','description']

# Register your models here.
#admin.site.register(WelcomeInfo)