from django.contrib import admin
from .models import Product

class ProductsAdmin(admin.ModelAdmin):

    list_display=['title','published'] #listeleme alanındaki gösterilecek kolonlar
    list_display_links=['published'] # listeleme alanındaki link verilen kolonlar
    list_filter=['published'] # sayfada filtreleme alanı
    search_fields=['title','content'] #arama alanlı
    list_editable=['title'] # editable belirlenen alanlar link olarak ayarlanmamalı!!! list filterden title alanını kaldırdım.
    


    class Meta:
        model =Product


# Register your models here.
admin.site.register(Product,ProductsAdmin)

# Register your models here.
