from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future, datetime_is_after_consent
from edc.base.model.models import BaseUuidModel
from edc.subject.appointment.models import Appointment

from .choices import VISIT_REASON
from .hnscc_off_study_mixin import HnsccOffStudyMixin


class HnsccVisit(HnsccOffStudyMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment,)

    report_datetime = models.DateTimeField(
        verbose_name="Visit Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_is_after_consent,
            datetime_not_future, ],
        help_text='Date and time of this report')

    reason = models.CharField(
        verbose_name="Reason for this visit?",
        max_length=25,
        choices=VISIT_REASON,
        help_text="", )

    history = AuditTrail()

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
        super(HnsccVisit, self).save(*args, **kwargs)

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Head & Neck Visit"
        verbose_name_plural = "Head & Neck Visit"
