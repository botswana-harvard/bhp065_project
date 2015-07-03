from django.contrib import admin

from edc.subject.appointment.admin import BaseAppointmentModelAdmin

from ..models import HnsccVisit, HnsccOffStudy
from ..forms.main import HnsccVisitForm, HnsccOffStudyForm
from .hnscc_off_study_model_admin import HnsccOffStudyModelAdmin


class HnsccVisitAdmin(BaseAppointmentModelAdmin):

    form = HnsccVisitForm
    visit_model_instance_field = 'hnscc_visit'
#     requisition_model = AnonymousRequisition
    dashboard_type = 'subject'
    date_heirarchy = 'report_datetime'
    list_display = (
        'appointment',
        'report_datetime',
        'reason',
        'created',
        'user_created',)
    list_filter = (
        'report_datetime',
        'reason',)
    search_fields = (
        'appointment__registered_subject__subject_identifier',)
    fields = (
        "appointment",
        "report_datetime",
        "reason",)
    radio_fields = {
        "reason": admin.VERTICAL}
admin.site.register(HnsccVisit, HnsccVisitAdmin)


class HnsccOffStudyAdmin(HnsccOffStudyModelAdmin):
    form = HnsccOffStudyForm
    fields = (
        "registered_subject",
        "hnscc_visit",
        "offstudy_date",
        "reason",)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "hnscc_visit":
            kwargs["queryset"] = HnsccVisit.objects.filter(id__exact=request.GET.get('hnscc_visit', 0))
        return super(HnsccOffStudyAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(HnsccOffStudy, HnsccOffStudyAdmin)
