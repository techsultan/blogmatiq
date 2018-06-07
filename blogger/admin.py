from django.contrib import admin
from blogger.models import (
    Blogger, Blog, BlogCategory, BlogPost, Comment
)

# Register your models here.
class BloggerAdmin(admin.ModelAdmin):
    fields = []

class BlogAdmin(admin.ModelAdmin):
    fields = []

class BlogCategoryAdmin(admin.ModelAdmin):
    fields = []

class BlogPostAdmin(admin.ModelAdmin):
    fields = []

class CommentAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)