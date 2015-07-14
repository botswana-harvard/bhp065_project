from django.contrib import admin

# from edc.base.modeladmin.admin import BaseModelAdmin
from edc.subject.appointment.admin import BaseAppointmentModelAdmin

from ..models import HnsccVisit, HnsccOffStudy
from ...hnscc_lab.models import HnsccRequisition
from ..forms import HnsccVisitForm, HnsccOffStudyForm
from .hnscc_off_study_model_admin import HnsccOffStudyModelAdmin


class HnsccVisitAdmin(BaseAppointmentModelAdmin):

    form = HnsccVisitForm
    visit_model_instance_field = 'hnscc_visit'
    requisition_model = HnsccRequisition
    dashboard_type = 'subject'
    date_heirarchy = 'report_datetime'
    list_display = (
        'appointment',
        'report_datetime',
        'data_type',
        'created',
        'user_created',)
    list_filter = (
        'report_datetime',
        'reason',
        'data_type',)
    search_fields = (
        'appointment__registered_subject__subject_identifier',)
    fields = (
        "appointment",
        "report_datetime",
        "reason",
        "data_type",)
    radio_fields = {
        "data_type": admin.VERTICAL}
admin.site.register(HnsccVisit, HnsccVisitAdmin)


class HnsccOffStudyAdmin(HnsccOffStudyModelAdmin):
    form = HnsccOffStudyForm
    fields = (
        "registered_subject",
        "hnscc_visit",
        "offstudy_date",
        "reason",
        "reason_other")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "hnscc_visit":
            kwargs["queryset"] = HnsccVisit.objects.filter(id__exact=request.GET.get('hnscc_visit', 0))
        return super(HnsccOffStudyAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(HnsccOffStudy, HnsccOffStudyAdmin)
