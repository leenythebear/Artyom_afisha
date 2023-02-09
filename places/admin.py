from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
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


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'place', 'number')


def preview(obj):
    return format_html(mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">'))
