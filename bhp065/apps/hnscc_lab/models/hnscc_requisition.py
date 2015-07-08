from django.core.urlresolvers import reverse
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.lab.lab_requisition.models import BaseRequisition

from ...hnscc_subject.models import HnsccVisit

from ..managers import HnsccRequisitionManager

from .aliquot_type import AliquotType
from .panel import Panel


class HnsccRequisition(BaseRequisition):

    hnscc_visit = models.ForeignKey(HnsccVisit)

    aliquot_type = models.ForeignKey(AliquotType)

    panel = models.ForeignKey(Panel)

    history = AuditTrail()

    entry_meta_data_manager = HnsccRequisitionManager(HnsccVisit)

    def save(self, *args, **kwargs):
        super(HnsccRequisition, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{0} {1}'.format(unicode(self.panel), self.requisition_identifier)

    def get_visit(self):
        return self.hnscc_visit

    @property
    def registered_subject(self):
        return self.hnscc_visit.appointment.registered_subject

    @property
    def visit_code(self):
        return self.hnscc_visit.appointment.visit_definition.code

    @property
    def optional_description(self):
        return ''

    def get_subject_identifier(self):
        return self.get_visit().subject_identifier

    def aliquot(self):
        url = reverse('admin:hnscc_lab_aliquot_changelist')
        return """<a href="{url}?q={requisition_identifier}" />aliquots</a>""".format(
            url=url, requisition_identifier=self.requisition_identifier)
    aliquot.allow_tags = True

    def dashboard(self):
        url = reverse('hnscc_dashboard_url',
                      kwargs={'dashboard_type': self.hnscc_visit.appointment.registered_subject.subject_type.lower(),
                              'dashboard_model': 'appointment',
                              'dashboard_id': self.hnscc_visit.appointment.pk,
                              'show': 'appointments'})
        return """<a href="{url}" />dashboard</a>""".format(url=url)
    dashboard.allow_tags = True

    class Meta:
        app_label = 'hnscc_lab'
        verbose_name = 'Patient Hnscc Requisition'
        unique_together = ('hnscc_visit', 'panel', 'is_drawn')
