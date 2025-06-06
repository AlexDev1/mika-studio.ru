from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from tinymce import HTMLField
from sorl.thumbnail import ImageField
from mika_studio.core.models import PageMeta


class Slider(models.Model):
    """Модель слайдера на Главной странице"""
    image = models.ImageField("Картинка", null=False)
    title = models.CharField("Название", max_length=255, null=False)
    subtitle = models.CharField("Подзаголовок", max_length=255, null=True, blank=True)
    link_name = models.CharField("Название кнопки", max_length=255, null=True, blank=True, default="Подробнее")
    url = models.URLField("Ссылка на страницу", null=True, blank=True)
    publish = models.BooleanField("Опубликованно", default=False)
    order = models.PositiveSmallIntegerField("Порядок", default=0, db_index=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды на главной"

    def __str__(self):
        return self.title


class Service(PageMeta):
    """Услуги"""
    image = models.ImageField('Картинка')
    subtitle = HTMLField("Описание", null=True, blank=True)
    price = models.CharField("Прайс", default=0, null=False,
                             help_text='Минимальный ценник на пример: От 1200 рублей за час', max_length=50)
    order = models.PositiveSmallIntegerField("Порядок", default=0, db_index=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe('<img width="100" src="%s" />' % escape(self.image.url))

    image_tag.short_description = 'Картинка'
    image_tag.allow_tags = True

    def get_absolut_url(self):
        return reverse('service-detail', args=[self.pk])

    def photos(self):
        return self.photoservices_set.all()


class PhotoServices(models.Model):
    """Фото для услуг"""
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    photo = models.ImageField("Фото", null=False, blank=False)
    title = models.CharField("Название", max_length=255, null=True, blank=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0, db_index=True)

    def __str__(self):
        return 'Фото {}'.format(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Фото'
        verbose_name_plural = "Фотографии в услуге"


class PriceServices(models.Model):
    """Прайс на услуги"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    days = models.CharField("Дни", blank=False, null=False, max_length=100, help_text='Например: пн-чт')
    price = models.PositiveSmallIntegerField("Прайс", default=0)
    time = models.CharField("Время", max_length=100, help_text="с 9.00 до 21.00", default="с 9.00 до 21.00")
    order = models.PositiveSmallIntegerField("Порядок", default=0, db_index=True)

    def __str__(self):
        return '{} - {} руб.'.format(self.days, self.price)

    class Meta:
        ordering = ['order']
        verbose_name = 'Прайс'
        verbose_name_plural = "Прайсы"


class ShowPrograms(PageMeta):
    """Шоу программы"""
    date_start = models.DateTimeField("Дата и время начала")
    description = models.TextField('Описание', max_length=1024)

    class Meta:
        ordering = ['date_start']
        verbose_name = "Шоу программа"
        verbose_name_plural = "Шоу программы"

    def __str__(self):
        return self.title


class PhotoGallery(models.Model):
    photo = ImageField("Фото", upload_to="photos")
    title = models.CharField("Название", max_length=255, blank=True, null=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0, db_index=True, blank=False, null=False)

    class Meta:
        ordering = ['order']
        verbose_name = "Фотография"
        verbose_name_plural = "Фотогалерея"

    def __str__(self):
        return self.title if self.title else '-'

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe('<img height="60" src="%s" />' % escape(self.photo.url))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True
