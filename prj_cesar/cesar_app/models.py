from django.db import models


class Word(models.Model):
    """ Model for word base

    """

    name = models.CharField(
        max_length=128,
        blank=False,
        verbose_name="Word's name",
    )

    def __str__(self):
        return '{0}'.format(self.name)
