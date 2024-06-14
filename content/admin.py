from django.contrib import admin

from .models import Blog, Category, Guide


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["slug", "name"]
    empty_value_display = "-empty-"


class GuideAdmin(admin.ModelAdmin):
    list_display = ["slug", "title"]
    empty_value_display = "-empty-"


class BlogAdmin(admin.ModelAdmin):
    list_display = ["slug", "title"]
    empty_value_display = "-empty-"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Blog, BlogAdmin)
