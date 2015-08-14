from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.off_study.models.base_off_study import BaseOffStudy
from edc.entry_meta_data.managers import EntryMetaDataManager

from .hnscc_visit import HnsccVisit


class HnsccOffStudy(BaseOffStudy):

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
