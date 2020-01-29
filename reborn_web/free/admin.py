from django.contrib import admin
from .models import Free, Comment


class FreeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'writer',
        'hits',
        'registered_date',
        )
    search_fields = ('title', 'content', 'writer__user_id',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post', 
        'content',
        'writer',
        'created',
        'updated',
        )
    search_fields = ('post__title', 'content', 'writer__user_id',)


admin.site.register(Free, FreeAdmin)
admin.site.register(Comment, CommentAdmin)