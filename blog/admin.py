from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # fields to display in the admin list view
    list_display = ("title", "author", "created_at", "updated_at", "is_published")

    # fields to display in the admin form view
    fields = ("title", "content", "author", "created_at", "updated_at", "is_published")

    readonly_fields = ("created_at", "updated_at")


admin.site.register(Post, PostAdmin)
