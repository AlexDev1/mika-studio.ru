from datetime import datetime

from django.db.models import Manager


class PublishManager(Manager):
    """Менаджер опубликованных обектов"""

    def all_objects(self):
        """Для Админки чтобы видно было все записи"""
        return super().get_queryset().all()

    def get_queryset(self):
        """Только опубликованные для всех запросов которые используют News.objects.filter(**)"""
        today = datetime.now()
        return super().get_queryset().filter(publish=True, date_published__lte=today)

    def unpublished_count(self):
        return super().get_queryset().filter(publish=False).count()

    def published(self):
        # from datetime import datetime
        today = datetime.now()
        return self.get_queryset().filter(publish=True, date_published__lte=today)
