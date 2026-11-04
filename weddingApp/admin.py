
from django.contrib import admin
from .models import WeddingProfile, GalleryImage


@admin.register(WeddingProfile)
class WeddingDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'bride_name',
        'groom_name',
        'wedding_date',
        'venue_name'
    )

@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):

    list_display = ('caption', 'order')
