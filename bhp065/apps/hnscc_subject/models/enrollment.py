from django.db import models
from django.conf import settings
from edc.audit.audit_trail import AuditTrail
from edc.base.model.validators import (datetime_not_before_study_start, datetime_not_future)
from edc.choices.common import GENDER
from edc.core.identifier.classes import SubjectIdentifier
from edc.base.model.models import BaseUuidModel
from edc.subject.appointment_helper.models import BaseAppointmentMixin
from edc.subject.registration.models import RegisteredSubject

from .hnscc_off_study_mixin import HnsccOffStudyMixin
from .choices import HIV_STATUS, SMOKING_STATUS


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

    history = AuditTrail()

    def __unicode__(self):
        return "{}, {}({})".format(self.registered_subject, self.gender, self.age)

    def enrollment_age(self):
        subject_age = []
        if self.age < 18:
            subject_age.append('Under age (<18).')
        return (False if subject_age else True, subject_age)

    @property
    def enrollment_response(self):
        age_response = []
        if self.age < 18:
            age_response.append('UNDER AGE.')
        age_response.sort()
        return '; '.join(age_response)

    def get_registration_datetime(self):
        return self.report_datetime

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollment"
