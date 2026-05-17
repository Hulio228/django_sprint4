from django.db.models import QuerySet
from django.utils import timezone


class CustomQuerySet(QuerySet):

    def publish_filter(self):
        return (self
                .select_related('author', 'category', 'location')
                .filter(
                    is_published=True,
                    pub_date__lte=timezone.now(),
                ))

    def category_filter(self):
        return self.publish_filter().filter(category__is_published=True)
