from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = [
        'image',
        'preview',
        'number',
    ]
    readonly_fields = ["preview"]

    @admin.display()
    def preview(self, obj):
        return preview(obj)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ('title', )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['image', 'preview', 'number']
    list_display = ('image', 'place', 'number')
    readonly_fields = ["preview"]

    @admin.display()
    def preview(self, obj):
        return preview(obj)


def preview(obj):
    return format_html(mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">'))
