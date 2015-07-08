from django.contrib import admin

from edc.lab.lab_requisition.admin import BaseRequisitionModelAdmin
from edc.export.actions import export_as_csv_action

from apps.hnscc_subject.models import HnsccVisit

from ..actions import print_requisition_label
from ..models import HnsccRequisition, Panel
from ..forms import HnsccRequisitionForm


class HnsccRequisitionAdmin(BaseRequisitionModelAdmin):

    def __init__(self, *args, **kwargs):
        super(HnsccRequisitionAdmin, self).__init__(*args, **kwargs)

    form = HnsccRequisitionForm
    visit_model = HnsccVisit
    visit_fieldname = 'hnscc_visit'
    dashboard_type = 'hnscc'

    label_template_name = 'requisition_label'
    actions = [print_requisition_label,
               export_as_csv_action("Export as csv", fields=[], delimiter=',', exclude=['id', 'revision',
                                                                                        'hostname_created',
                                                                                        'hostname_modified',
                                                                                        'user_created',
                                                                                        'user_modified'],)]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        panel_pk = request.GET.get('panel', 0)
        if db_field.name == 'panel':
            kwargs["queryset"] = Panel.objects.filter(pk=panel_pk)
        if db_field.name == 'aliquot_type':
            if Panel.objects.filter(pk=panel_pk):
                if Panel.objects.get(pk=panel_pk).aliquot_type.all():
                    kwargs["queryset"] = Panel.objects.get(pk=panel_pk).aliquot_type.all()
        return super(BaseRequisitionModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(HnsccRequisition, HnsccRequisitionAdmin)
