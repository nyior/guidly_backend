from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Blog, Category, Guide


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["slug", "name"]
    empty_value_display = "-empty-"


class GuideAdmin(admin.ModelAdmin):
    list_display = ["slug", "title"]
    empty_value_display = "-empty-"
    date_hierarchy = "last_updated"


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ["slug", "title"]
    empty_value_display = "-empty-"
    date_hierarchy = "last_updated"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Blog, BlogAdmin)
