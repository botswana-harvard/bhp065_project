# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel


class Contemporary (BaseScheduledVisitModel):

    pathology_no = models.CharField(
        verbose_name="Pathology",
        max_length=15,
        help_text="", )
    diagnosis_date = models.DateField(
        verbose_name="Date of Diagnosis",
        help_text="", )
    specimen_collecton = models.DateField(
        verbose_name="Specimen Collection",
        help_text="", )
    specimen_size = models.CharField(
        verbose_name="Specimen size",
        max_length=25,
        help_text="", )
    nature_of_specimen = models.CharField(
        verbose_name="Nature of specimen",
        max_length=45,
        help_text="", )
    tissues = models.CharField(
        verbose_name="Tissues",
        max_length=45,
        help_text="", )
    topography_code = models.CharField(
        max_length=15,
        verbose_name="Cancer Site",
        validators=[RegexValidator(
            regex=r'^([C](\d{2})|[C](\d{2}\.\d{1}))$',
            message=('A site code always starts with a C, followed by numbers: integer or'
                     'decimal.FORMAT is CXX or CXX.X')), ],
        help_text="record ICD topography code", )
    morphology_code = models.CharField(
        max_length=15,
        verbose_name="Clinical and/or Pathologic Diagnosis",
        validators=[RegexValidator(
            regex=r'^[M]{1}[0-9]{4}[/][3]{1}$',
            message='A site code always starts with a M, followed by four numbers and a /3'), ],
        help_text="record ICD morphology code", )
    diagnosis = models.TextField(
        verbose_name="Diagnosis",
        max_length=150,
        help_text="", )
    any_duplications = models.CharField(
        verbose_name="Any sample duplications?",
        max_length=3,
        choices=YES_NO, )

    history = AuditTrail()

    def get_visit(self):
        return self.hnscc_visit

    def __unicode__(self):
        return unicode(self.hnscc_visit)

    def get_absolute_url(self):
        return reverse('admin:hnscc_subject_contemporary_change', args=(self.id,))

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Contemporary"
        verbose_name_plural = "Contemporary"
