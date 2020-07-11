from django.contrib import admin
from .models import Chapter

@admin.register(Chapter)
class TutorialsAdmin(admin.ModelAdmin):
    list_display=['chapter','title','description']

# Register your models here.
