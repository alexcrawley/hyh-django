#-*- coding: utf-8 -*-
from django.conf import settings

from apps.events.tevo_services import TevoService


class BaseTevoModelService(object):
    def update_from_tevo(self, propogate_related=False):
        api = TevoService().get_api()

        resource_url = "%s%s%d" % (
            settings.TICKET_EVOLUTION_URL_PREFIX,
            self.tevo_resource_name,
            self.tevo_id
            )

        result = api.get(resource_url)

        for tevo_field in self.tevo_fields:
            value = result.get(tevo_field, None)

            if value is not None:
                setattr(self, tevo_field, value)

        # Commit the changes
        self.save()

        return self
