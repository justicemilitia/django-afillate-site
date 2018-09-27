from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product


def get_picture_preview(obj):
    if obj.pk:  # if object has already been saved and has a primary key, show picture preview
        return mark_safe("""<a href="{src}" target="_blank"><img src="http://127.0.0.1:5000/static/images/products/{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
            src=obj.image,
            title=obj.title,
        ))
    return ("(choose a picture and save and continue editing to see the preview)")


get_picture_preview.allow_tags = True
get_picture_preview.short_description = ("Picture Preview")


class ProductsAdmin(admin.ModelAdmin):

    # listeleme alanındaki gösterilecek kolonlar
    list_display = ['title', 'image', 'price', 'published']
    # listeleme alanındaki link verilen kolonlar
    list_display_links = ['published', 'image', 'price']
    list_filter = ['published']  # sayfada filtreleme alanı
    search_fields = ['title', 'content']  # arama alanlı
    # editable belirlenen alanlar link olarak ayarlanmamalı!!! list filterden title alanını kaldırdım.
    list_editable = ['title']
    # save_on_top = True
    fields = ['title', 'image', 'content','slug','price', get_picture_preview,'link','published','sort','urli']
    readonly_fields = [get_picture_preview]
    # inlines = [ReviewInline]

    class Meta:
        model = Product


# Register your models here.
admin.site.register(Product, ProductsAdmin)

# Register your models here.
