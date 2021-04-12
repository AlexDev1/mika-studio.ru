from django import template
from django.core.cache import cache

from mika_studio.settings.models import Service, Slider, PhotoGallery

register = template.Library()


@register.simple_tag
def get_menu_services():
    return Service.objects.filter(publish=True)


@register.simple_tag
def get_slider():
    return Slider.objects.filter(publish=True)


@register.simple_tag
def get_gallery():
    return PhotoGallery.objects.all()
