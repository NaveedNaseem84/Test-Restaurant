from django.contrib import admin
from .models import WelcomeInfo
from django_summernote.admin import SummernoteModelAdmin

@admin.register(WelcomeInfo)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('promotion_title', 'is_valid')
    search_fields = ['promotion_title','description']

# Register your models here.
#admin.site.register(WelcomeInfo)