from django.db import models
from apps.core import models as mod_core
# from apps.core.models import News, News_comment, Event, Event_comment

# from apps.blog import models as mod_blog

class PublishedNewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=mod_core.News.Status.PUBLİSHED)


class PublishedNewsCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=mod_core.News_comment.Status.PUBLİSHED)
    

class PublishedEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=mod_core.Event.Status.PUBLİSHED)



class PublishedEventCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=mod_core.Event_comment.Status.PUBLİSHED)


