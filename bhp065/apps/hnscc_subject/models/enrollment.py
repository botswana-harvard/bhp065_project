from django.db import models
from django.conf import settings

from edc.audit.audit_trail import AuditTrail
from edc.base.model.models import BaseUuidModel
from edc.base.model.validators import (datetime_not_before_study_start, datetime_not_future)
from edc.choices.common import GENDER
from edc.choices.common import YES_NO
from edc.core.identifier.classes import SubjectIdentifier
from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.registration.models import RegisteredSubject

from .choices import HIV_STATUS, SMOKING_STATUS
from .hnscc_off_study_mixin import HnsccOffStudyMixin


class Enrollment (HnsccOffStudyMixin, BaseAppointmentMixin, BaseUuidModel):

    """This is the subject enrollment form"""

    registered_subject = models.OneToOneField(RegisteredSubject, editable=False, null=True)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        help_text='Date and time of collection')

    gender = models.CharField(
        verbose_name='Gender',
        max_length=1,
        choices=GENDER)

    age = models.IntegerField(
        verbose_name='Age in years',
        null=True,
        blank=True,
        help_text='')

    hiv_status = models.CharField(
        verbose_name='HIV status',
        max_length=25,
        choices=HIV_STATUS,
        help_text="")

    smoking_status = models.CharField(
        verbose_name='Smoking status',
        max_length=15,
        choices=SMOKING_STATUS,)

    bpcc_enrolled = models.CharField(
        verbose_name='BPCC enrolled',
        max_length=3,
        choices=YES_NO,
        help_text="Botswana Prospective Cancer Cohort", )

    bid_number = models.CharField(
        verbose_name="BPCC BID number",
        max_length=15,
        null=True,
        blank=True,
        help_text="this is only for those who are registered on the BPCC/BHP045 cohort", )

    history = AuditTrail()

    def __unicode__(self):
        return "{}, {}({})".format(self.registered_subject, self.gender, self.age)

    def get_registration_datetime(self):
        return self.report_datetime

    def save(self, *args, **kwargs):
        using = kwargs.get('using')
        self.register_enrolled_subjects(using)
        super(Enrollment, self).save(*args, **kwargs)

    def register_enrolled_subjects(self, using, **kwargs):
        registered_subject = RegisteredSubject.objects.using(using).create(
            created=self.created,
            subject_identifier=SubjectIdentifier(site_code=settings.SITE_CODE).get_identifier(),
            first_name='Anonymous',
            gender=self.gender,
            hiv_status=self.hiv_status,
            subject_type='subject',
            registration_datetime=self.created,
            user_created=self.user_created,
            registration_status='enrolled',)
        self.registered_subject = registered_subject

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollment"
