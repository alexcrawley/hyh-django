#-*- coding: utf-8 -*-


class ExperimentTestGroupService(object):
    def get_next_test_group(self):
        return self.test_groups.order_by('-num_users')[0]


class ExperimentServices(ExperimentTestGroupService):
    """ Container for all experiment service mixins.
    """
    pass
