from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "status",
        "created_on",
    )  # Display these fields in the admin list view
    list_filter = ("status", "author")  # Add filters for status and author
    search_fields = ("title", "content")  # Enable search by title and content
    ordering = ("-created_on",)  # Order posts by creation date (newest first)
