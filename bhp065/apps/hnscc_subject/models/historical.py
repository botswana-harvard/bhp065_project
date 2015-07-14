# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel
from .choices import HOSPITAL


class Historical (BaseScheduledVisitModel):

    serial = models.IntegerField(
        verbose_name="Serial",
        max_length=5,
        help_text="", )
    received = models.DateField(
        verbose_name="Received",
        help_text="to use as specimen collect date", )
    histo_no = models.IntegerField(
        verbose_name="Historical number",
        max_length=10,
        help_text="", )
    pathology_no = models.CharField(
        verbose_name="Pathology Number",
        max_length=15,
        help_text="", )
    hospital = models.CharField(
        verbose_name="Hospital",
        max_length=35,
        choices=HOSPITAL)
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
    clinical_dx = models.TextField(
        verbose_name="Clinical Diagnosis",
        max_length=150,
        help_text="", )
    final_dx = models.TextField(
        verbose_name="Final Diagnosis",
        max_length=150, )
    diagnosis_date = models.DateField(
        verbose_name="Date of Diagnosis",
        help_text="", )
    topography_code = models.CharField(
        verbose_name="Cancer Site",
        max_length=15,
        validators=[RegexValidator(
            regex=r'^([C](\d{2})|[C](\d{2}\.\d{1}))$',
            message=('A site code always starts with a C, followed by numbers: integer or '
                     'decimal.FORMAT is CXX or CXX.X')), ],
        help_text="record ICD topography code", )
    morphology_code = models.CharField(
        verbose_name="Clinical and/or Pathologic Diagnosis",
        max_length=15,
        validators=[RegexValidator(
            regex=r'^[M]{1}[0-9]{4}[/][3]{1}$',
            message='A site code always starts with a M, followed by four numbers and a /3'), ],
        help_text="record ICD morphology code", )
    no_of_blocks = models.IntegerField(
        verbose_name="Number of blocks",
        max_length=3,
        null=True,
        blank=True,
        help_text="", )

    history = AuditTrail()

    def get_visit(self):
        return self.hnscc_visit

    def __unicode__(self):
        return unicode(self.hnscc_visit)

    def get_absolute_url(self):
        return reverse('admin:hnscc_subject_historical_change', args=(self.id,))

    class Meta:
        app_label = "hnscc_subject"
        verbose_name = "Historical"
        verbose_name_plural = "Historical"
