from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display=['title','publishing_date'] #listeleme alanındaki gösterilecek kolonlar
    list_display_links=['publishing_date'] # listeleme alanındaki link verilen kolonlar
    list_filter=['publishing_date'] # sayfada filtreleme alanı
    search_fields=['title','content'] #arama alanlı
    list_editable=['title'] # editable belirlenen alanlar link olarak ayarlanmamalı!!! list filterden title alanını kaldırdım.
    


    class Meta:
        model =Post


# Register your models here.
admin.site.register(Post,PostAdmin)
