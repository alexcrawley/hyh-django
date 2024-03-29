from django.contrib import admin

from apps.experiments.models import Experiment, TestGroup


class TestGroupAdmin(admin.ModelAdmin):
    model = TestGroup


class TestGroupInline(admin.TabularInline):
    model = TestGroup
    readonly_fields = ['num_users']
    fields = ['algorithm', 'num_users']
    extra = 1


class ExperimentAdmin(admin.ModelAdmin):
    inlines = [TestGroupInline]

    list_display = [
        'name',
        'experiment_type',
        'population_percentage',
        ]

    list_filter = [
        'experiment_type',
        ]

    search_fields = [
        'name'
        ]


admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(TestGroup, TestGroupAdmin)
