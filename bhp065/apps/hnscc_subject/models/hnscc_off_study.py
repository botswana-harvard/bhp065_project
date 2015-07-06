from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.device.sync.models import BaseSyncUuidModel
from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.registration.models import RegisteredSubject
from edc.entry_meta_data.managers import EntryMetaDataManager

from .choices import OFF_STUDY_REASON
from .hnscc_visit import HnsccVisit


class HnsccOffStudy(BaseSyncUuidModel, BaseAppointmentMixin):

    registered_subject = models.OneToOneField(RegisteredSubject)

    offstudy_date = models.DateField(
        verbose_name="Off-study Date",
        help_text="")

    reason = models.CharField(
        verbose_name="Please code the primary reason participant taken off-study",
        choices=OFF_STUDY_REASON,
        max_length=45)

    history = AuditTrail()

    hnscc_visit = models.OneToOneField(HnsccVisit)

    entry_meta_data_manager = EntryMetaDataManager(HnsccVisit)

    def __unicode__(self):
        return '%s ' % (self.registered_subject)

    def get_visit(self):
        return self.hnscc_visit

    def get_absolute_url(self):
        return reverse('admin:hnscc_subject_hnsccoffstudy_change', args=(self.id,))

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Head & Neck Off Study"
        verbose_name_plural = "Head & Neck Off Study"
