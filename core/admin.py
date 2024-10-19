from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from core.models import Video, Tag


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('num_likes', 'num_views', 'published_at', 'author')
    list_display = ('title', 'is_published', 'num_likes',
                    'num_views', 'published_at')
    search_fields = ('title', 'tags__name')
    list_filter = ('is_published', 'tags')

    def save_model(self, request: HttpRequest, obj: Video, form: ModelForm, change: bool) -> None:
        if not obj.pk:
            # Assuming user is logged in and assigned to obj.author.
            obj.author = request.user
        return super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
