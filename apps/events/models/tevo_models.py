#-*- coding: utf-8 -*-
from django.conf import settings

from apps.common import models
from apps.events.models.model_services import BaseTevoModelService
from apps.events.tevo_services import TevoService


class TevoBaseManager(models.Manager):
    def create_or_update(self, tevo_id, fields_dict=None, propogate_related=True):
        try:
            instance = self.model.objects.get(tevo_id=tevo_id)
        except self.model.DoesNotExist:
            instance = self.model(tevo_id=tevo_id)

        if fields_dict is not None:
            return instance.update_from_dict(fields_dict, propogate_related)
        else:
            return instance.update_from_tevo(propogate_related)

    def tevo_list(self, list_params={}, page=None):
        api = TevoService().get_api()

        resource_url = "%s/%s" % (
            settings.TICKET_EVOLUTION_URL_PREFIX,
            self.model.tevo_resource_name
            )

        return api.get(resource_url, parameters=list_params)

    def update_from_tevo(self, list_params={}, all_pages=True):
        tevo_list = self.tevo_list(list_params)

        while tevo_list[self.model.tevo_resource_name]:
            page_num = tevo_list['current_page']

            print(tevo_list['current_page'])

            for tevo_dict in tevo_list[self.model.tevo_resource_name]:
                if tevo_dict.get('id', False):
                    self.create_or_update(
                        tevo_id=tevo_dict['id'], fields_dict=tevo_dict)

            if not all_pages:
                break

            list_params['page'] = int(page_num) + 1

            tevo_list = self.tevo_list(list_params)


class TevoBase(models.Model, BaseTevoModelService):
    tevo_id = models.IntegerField(unique=True)

    tevo_resource_name = None
    tevo_fields = ()
    tevo_related_fields_map = {}

    objects = TevoBaseManager()

    class Meta:
        abstract = True


class TevoCategory(TevoBase):
    tevo_resource_name = 'categories'

    parent = models.ForeignKey('TevoCategory', null=True)

    # Core Fields
    name = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000)

    def __init__(self, *args, **kwargs):
        self.tevo_fields = ('name', 'slug',)
        self.tevo_related_fields_map = {
            'parent': self.__class__,
            }

        return super(TevoCategory, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.name


class TevoPerformer(TevoBase):
    pass


class TevoConfiguration(TevoBase):
    pass


class TevoVenue(TevoBase):
    pass


class TevoEvent(TevoBase):
    tevo_resource_name = 'events'
    tevo_fields = ('name', 'occurs_at', 'state', 'stubhub_id',
                   'owned_by_office', 'available_count', 'products_count',
                   'popularity_score', 'long_term_popularity_score')

    tevo_related_fields_map = {
        'category': TevoCategory,
        'venue': TevoVenue,
        'configuration': TevoConfiguration,
        }

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

    def __unicode__(self):
        return self.name


class TevoClient(TevoBase):
    pass
