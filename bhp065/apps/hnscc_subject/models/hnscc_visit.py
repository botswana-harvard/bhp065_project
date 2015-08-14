from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
# from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent
# from edc.base.model.models import BaseUuidModel
from edc.subject.visit_tracking.models import BaseVisitTracking
from edc.subject.entry.models import Entry
from edc.entry_meta_data.models import ScheduledEntryMetaData
# from edc.subject.appointment.models import Appointment

from .choices import VISIT_REASON, DATA_COLLECTION_TYPE
from .hnscc_off_study_mixin import HnsccOffStudyMixin


class HnsccVisit(HnsccOffStudyMixin, BaseVisitTracking):

    data_type = models.CharField(
        verbose_name="Type of data collection",
        max_length=25,
        choices=DATA_COLLECTION_TYPE, )
#
#     appointment = models.OneToOneField(Appointment,)
#
#     report_datetime = models.DateTimeField(
#         verbose_name="Visit Date and Time",
#         validators=[
#             datetime_not_before_study_start,
#             datetime_is_after_consent,
#             datetime_not_future, ],
#         help_text='Date and time of this report')
#
#     reason = models.CharField(
#         verbose_name="Reason for this visit?",
#         max_length=25,
#         choices=VISIT_REASON,
#         help_text="", )

    history = AuditTrail()

    def get_visit_reason_choices(self):
        return VISIT_REASON

    @property
    def registered_subject(self):
        return self.get_registered_subject()

    def get_appointment(self):
        return self.appointment

    def __unicode__(self):
        return unicode(self.appointment)

    def get_absolute_url(self):
        return reverse('admin:hnscc_subject_hnsccvisit_change', args=(self.id,))

    def save(self, *args, **kwargs):
        self.create_off_study_meta()
        # self.contemporary_meta()
        # self.historical_meta()
        super(HnsccVisit, self).save(*args, **kwargs)

    def create_off_study_meta(self):
        if self.reason == 'off study':
            entry = Entry.objects.filter(model_name='hnsccoffstudy',
                                         visit_definition_id=self.appointment.visit_definition_id)
            if entry:
                scheduled_meta_data = ScheduledEntryMetaData.objects.filter(
                    appointment=self.appointment,
                    entry=entry[0],
                    registered_subject=self.registered_subject)
                if not scheduled_meta_data:
                    scheduled_meta_data = ScheduledEntryMetaData.objects.create(
                        appointment=self.appointment,
                        entry=entry[0],
                        registered_subject=self.registered_subject)
                else:
                    scheduled_meta_data = scheduled_meta_data[0]
                scheduled_meta_data.entry_status = 'NEW'
                scheduled_meta_data.save()

#     def contemporary_meta(self):
#         if self.data_type == 'contemporary':
#             entry = Entry.objects.filter(model_name='historical',
#                                          visit_definition_id=self.appointment.visit_definition_id)
#             if entry:
#                 scheduled_meta_data = ScheduledEntryMetaData.objects.filter(
#                     appointment=self.appointment,
#                     entry=entry[0],
#                     registered_subject=self.registered_subject)
#                 if not scheduled_meta_data:
#                     scheduled_meta_data = ScheduledEntryMetaData.objects.create(
#                         appointment=self.appointment,
#                         entry=entry[0],
#                         registered_subject=self.registered_subject)
#                 else:
#                     scheduled_meta_data = scheduled_meta_data[0]
#                 scheduled_meta_data.entry_status = 'NOT REQUIRED'
#                 scheduled_meta_data.save()
#         if not self.data_type == 'contemporary':
#             entry = Entry.objects.filter(model_name='historical',
#                                          visit_definition_id=self.appointment.visit_definition_id)
#             if entry:
#                 scheduled_meta_data = ScheduledEntryMetaData.objects.filter(
#                     appointment=self.appointment,
#                     entry=entry[0],
#                     registered_subject=self.registered_subject)
#                 if not scheduled_meta_data:
#                     scheduled_meta_data = ScheduledEntryMetaData.objects.create(
#                         appointment=self.appointment,
#                         entry=entry[0],
#                         registered_subject=self.registered_subject)
#                 else:
#                     scheduled_meta_data = scheduled_meta_data[0]
#                 scheduled_meta_data.entry_status = 'NEW'
#                 scheduled_meta_data.save()
#
#     def historical_meta(self):
#         if self.data_type == 'historical':
#             entry = Entry.objects.filter(model_name='contemporary',
#                                          visit_definition_id=self.appointment.visit_definition_id)
#             if entry:
#                 scheduled_meta_data = ScheduledEntryMetaData.objects.filter(
#                     appointment=self.appointment,
#                     entry=entry[0],
#                     registered_subject=self.registered_subject)
#                 if not scheduled_meta_data:
#                     scheduled_meta_data = ScheduledEntryMetaData.objects.create(
#                         appointment=self.appointment,
#                         entry=entry[0],
#                         registered_subject=self.registered_subject)
#                 else:
#                     scheduled_meta_data = scheduled_meta_data[0]
#                 scheduled_meta_data.entry_status = 'NOT REQUIRED'
#                 scheduled_meta_data.save()
#         if not self.data_type == 'historical':
#             entry = Entry.objects.filter(model_name='contemporary',
#                                          visit_definition_id=self.appointment.visit_definition_id)
#             if entry:
#                 scheduled_meta_data = ScheduledEntryMetaData.objects.filter(
#                     appointment=self.appointment,
#                     entry=entry[0],
#                     registered_subject=self.registered_subject)
#                 if not scheduled_meta_data:
#                     scheduled_meta_data = ScheduledEntryMetaData.objects.create(
#                         appointment=self.appointment,
#                         entry=entry[0],
#                         registered_subject=self.registered_subject)
#                 else:
#                     scheduled_meta_data = scheduled_meta_data[0]
#                 scheduled_meta_data.entry_status = 'NEW'
#                 scheduled_meta_data.save()

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Head & Neck Visit"
        verbose_name_plural = "Head & Neck Visit"
