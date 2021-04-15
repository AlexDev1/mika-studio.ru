from django.db import models
from django.utils.safestring import mark_safe

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
    subtitle = models.TextField("Описание", max_length=255, null=True, blank=True)
    price = models.CharField("Прайс", default=0, null=False,
                             help_text='Минимальный ценник на пример: От 1200 рублей за час', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe('<img width="150" src="%s" />' % escape(self.image.url))

    image_tag.short_description = 'Картинка'
    image_tag.allow_tags = True


class PriceServices(models.Model):
    """Прайс на услуги"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    days = models.CharField("Дни", blank=False, null=False, max_length=100, help_text='Например: пн-чт')
    price = models.PositiveSmallIntegerField("Прайс", default=0)
    time = models.CharField("Время", max_length=100, help_text="с 9.00 до 21.00", default="с 9.00 до 21.00")

    def __str__(self):
        return '{} - {} руб.'.format(self.days, self.price)

    class Meta:
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
    photo = models.ImageField("Фото")
    title = models.CharField("Название", max_length=255)
    order = models.PositiveSmallIntegerField("Порядок", default=0, db_index=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Фотография"
        verbose_name_plural = "Фотогалерея"

    def __str__(self):
        return self.title
