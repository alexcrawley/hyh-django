from django.contrib import admin

from apps.experiments.models import Experiment, TestGroup


class TestGroupInline(admin.TabularInline):
    model = TestGroup
    readonly_fields = ['num_users']
    fields = ['algorithm', 'num_users', 'target_percentage']
    extra = 1


class ExperimentAdmin(admin.ModelAdmin):
    inlines = [TestGroupInline]
    list_display = [
        'name',
        'experiment_type',
        'population_percentage',
        'start_date',
        'end_date'
        ]


admin.site.register(Experiment, ExperimentAdmin)