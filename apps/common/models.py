from django.db.models import *


class ValidateModel(Model):

    def save(self, *args, **kwrags):
        self.full_clean()
        return super(ValidateModel, self).save(*args, **kwrags)

    class Meta:
        abstract = True
