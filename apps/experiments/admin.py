from django.contrib import admin

from apps.experiments.models import Experiment, TestGroup


class TestGroupInline(admin.TabularInline):
    model = TestGroup
    readonly_fields = ['num_users']
    fields = ['algorithm', 'num_users', 'target_percentage']
    extra = 1


class ExperimentAdmin(admin.ModelAdmin):
    inlines = [TestGroupInline]


admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(TestGroup)
