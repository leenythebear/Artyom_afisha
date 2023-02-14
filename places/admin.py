from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

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
    return format_html("<img src={} style='max-height: 200px;'>", obj.image.url)
