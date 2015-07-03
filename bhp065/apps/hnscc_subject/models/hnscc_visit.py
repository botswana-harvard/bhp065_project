from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent
from edc.device.sync.models import BaseSyncUuidModel
from edc.subject.appointment.models import Appointment

from .choices import VISIT_REASON
from .hnscc_off_study_mixin import HnsccOffStudyMixin


class HnsccVisit(HnsccOffStudyMixin, BaseSyncUuidModel):

    appointment = models.OneToOneField(Appointment,)

    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future, ],
        help_text='Date and time of this report')

    history = AuditTrail()

    @property
    def registered_subject(self):
        return self.get_registered_subject()

    def __unicode__(self):
        return unicode(self.appointment)

    def get_absolute_url(self):
        return reverse('admin:hnscc_subject_hnsccvisit_change', args=(self.id,))

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def save(self, *args, **kwargs):
        super(HnsccVisit, self).save(*args, **kwargs)

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Head & Neck Visit"
        verbose_name_plural = "Head & Neck Visit"
