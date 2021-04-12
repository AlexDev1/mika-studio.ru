from django.db import models


class PageMeta(models.Model):
    """Абстрактная модель для мета тегов"""
    title = models.CharField("Название", max_length=255)
    create_dt = models.DateTimeField("Созданно", auto_now_add=True)
    publish = models.BooleanField("Опубликованно", default=False)
    order = models.PositiveSmallIntegerField("Порядок", default=0, db_index=True)
    seo_title = models.CharField('Заголовок', max_length=1024)
    seo_keywords = models.CharField('Ключевые слова страницы', blank=True, max_length=1024)
    seo_description = models.CharField('Мета описание', blank=True, max_length=1024)

    class Meta:
        abstract = True
