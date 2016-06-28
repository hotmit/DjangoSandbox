from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class MultiKey(models.Model):
    actor_type = models.ForeignKey(ContentType, related_name='actor_type_activities')
    actor_id = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_type', 'actor_id')

    def __str__(self):
        return '%s, %s' % (self.actor_type_id, self.actor_id)
