from django.db import models
from tinymce import HTMLField

from mika_studio.settings.mixins import ObjectSimpleMixin


class PageContent(ObjectSimpleMixin):
    content = HTMLField("Описание")

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = 'Страницы'


class Event(ObjectSimpleMixin):
    page = models.ForeignKey(PageContent, on_delete=models.CASCADE)
    desc = HTMLField("Описание")
    order = models.PositiveSmallIntegerField("н/п", default=0, db_index=True)
    date_event = models.DateTimeField("Дата и время мероприятия")

    class Meta:
        ordering = ['order']
        verbose_name = "Мероприятие"
        verbose_name_plural = 'Мероприятия'

