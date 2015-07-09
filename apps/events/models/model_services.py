#-*- coding: utf-8 -*-
from django.conf import settings

from apps.events.tevo_services import TevoService


class BaseTevoModelService(object):
    def update_from_tevo(self, propogate_related=False):
        api = TevoService().get_api()

        resource_url = "%s/%s/%d" % (
            settings.TICKET_EVOLUTION_URL_PREFIX,
            self.tevo_resource_name,
            self.tevo_id
            )

        result = api.get(resource_url)

        # Copy fields to model
        return self.update_from_dict(result, propogate_related)

    def update_from_dict(self, fields_dict, propogate_related):
        for tevo_field in self.tevo_fields:
            value = fields_dict.get(tevo_field, None)

            if value is not None:
                setattr(self, tevo_field, value)

        if propogate_related:
            # Also create/ update related fields.
            for tevo_related_field in self.tevo_related_fields_map.keys():
                values_dict = fields_dict.get(tevo_related_field, None)
                if values_dict is not None:
                    RelatedTevoModel = self.tevo_related_fields_map.get(
                        tevo_related_field)

                    instance = RelatedTevoModel.objects.create_or_update(
                        int(values_dict['id']), values_dict)

                    setattr(self, tevo_related_field, instance)

        # Commit the changes
        self.save()

        return self
