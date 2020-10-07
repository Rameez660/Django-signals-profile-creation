from django.contrib import admin
from .models import Profile,Description,Commment
# Register your models here.
admin.site.register(Profile)
# admin.site.register(Description)


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('user','title','desc')

@admin.register(Commment)
class CommmentAdmin(admin.ModelAdmin):
    list_display = ('profile','description','comment_text')
