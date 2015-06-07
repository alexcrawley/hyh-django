from apps.common import models

from apps.events.models.model_services import BaseTevoModelService


class TevoBaseManager(models.Manager):
    def create_or_update_from_id(self, tevo_id):
        try:
            instance = self.model.objects.get(tevo_id=tevo_id)
        except self.model.DoesNotExist:
            instance = self.model(tevo_id=tevo_id)

        return instance.update_from_tevo()


class TevoBase(models.Model, BaseTevoModelService):
    tevo_id = models.IntegerField(unique=True)
    tevo_url = models.URLField(unique=True)

    tevo_fields = ()
    tevo_related_fields = ()

    objects = TevoBaseManager()

    class Meta:
        abstract = True


class TevoCategory(TevoBase):
    pass


class TevoPerformer(TevoBase):
    pass


class TevoConfiguration(TevoBase):
    pass


class TevoVenue(TevoBase):
    pass


class TevoEvent(TevoBase):
    tevo_resource_name = '/events/'
    tevo_fields = ('name', 'occurs_at', 'state', 'stubhub_id',
                   'owned_by_office', 'available_count', 'products_count',
                   'popularity_score', 'long_term_popularity_score')

    tevo_related_fields = ('category', 'venue', 'configuration', 'performers')

    # Core Fields
    name = models.CharField(max_length=1000)
    occurs_at = models.DateTimeField()
    state = models.CharField(max_length=1000)
    stubhub_id = models.CharField(max_length=1000)

    owned_by_office = models.BooleanField(default=False)

    available_count = models.IntegerField()
    products_count = models.IntegerField()

    popularity_score = models.DecimalField(
        max_digits=20, decimal_places=6)
    long_term_popularity_score = models.DecimalField(
        max_digits=20, decimal_places=6)

    # Related Fields
    category = models.ForeignKey(TevoCategory, null=True)
    venue = models.ForeignKey(TevoVenue, null=True)
    configuration = models.ForeignKey(TevoConfiguration, null=True)
    performers = models.ManyToManyField(TevoPerformer, null=True)


class TevoClient(TevoBase):
    pass
