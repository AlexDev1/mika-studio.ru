from django.contrib import admin

from mika_studio.settings.models import Slider, Service, PriceServices, ShowPrograms, PhotoGallery, PhotoServices


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title']


class PriceAdmin(admin.TabularInline):
    model = PriceServices
    extra = 0


class PhotoServicesAdmin(admin.TabularInline):
    model = PhotoServices
    extra = 0

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["image_tag", 'title', 'publish']
    inlines = [PriceAdmin, PhotoServicesAdmin]
    fields = ('title', 'image_tag', 'image', 'subtitle', 'price', 'publish')
    readonly_fields = ('image_tag',)

@admin.register(ShowPrograms)
class ShowProgramsAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    pass
