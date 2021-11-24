from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from tagging_autocomplete.models import TagAutocompleteField

from mika_studio.settings.managers import PublishManager


class TimeStampMixin(models.Model):
    """Миксин дат(создано-изменено)"""
    created_value = models.DateTimeField("Создано", auto_now_add=True)
    modified_value = models.DateTimeField("Изменено", auto_now=True)

    class Meta:
        abstract = True


class SEOMetaMixin(models.Model):
    """SEO Mixin"""
    meta_title = models.CharField("SEO Title", max_length=255, blank=True, null=True)
    meta_description = models.TextField("Meta Description", blank=True, null=True)
    meta_keywords = models.CharField(
        "Meta Keywords", blank=True, null=True, max_length=255
    )

    class Meta:
        abstract = True


class ObjectSimpleMixin(TimeStampMixin, SEOMetaMixin, models.Model):
    """
    Миксин для обектов:
    title: Основное название объекта,
    publish: Настройка публикации объекта,
    timestamp: Штампы времени,
    seo meta: seo данные для страницы,
    tags: Теги для обекта,
    hitcount: Подсчет хитов,
    history: Используется для ведения истории изменения объекта,
    """
    title = models.CharField("Название", max_length=255)

    # Settings published object
    publish = models.BooleanField("Опубликованно", default=True, db_index=True)
    date_published = models.DateTimeField("Дата публикации")

    slug = AutoSlugField(populate_from="title")
    tags = TagAutocompleteField(
        blank=True,
        verbose_name="Теги для объекта",
        help_text="Чтобы использовать тег из 2-х и более слов, нужно вставлять в ковычки",
    )

    allobjects = models.Manager()
    objects = PublishManager()

    # Track History
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def is_publish(self):
        if (self.date_published <= timezone.now()) & (self.publish is True):
            return True
        else:
            return False
