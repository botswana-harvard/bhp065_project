from datetime import datetime
from django.db import models

from edc.base.model.validators import datetime_not_before_study_start, datetime_not_future
from edc.entry_meta_data.managers import EntryMetaDataManager

from ..models.hnscc_visit import HnsccVisit
from .hnscc_base_uuid_model import HnsccBaseUuidModel
from ..managers import ScheduledModelManager


class BaseScheduledVisitModel(HnsccBaseUuidModel):

    """ Base model for all scheduled models"""

    hnscc_visit = models.OneToOneField(HnsccVisit)

    entry_meta_data_manager = EntryMetaDataManager(HnsccVisit)

    report_datetime = models.DateTimeField(
        "Today's date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=datetime.today(), )

    objects = ScheduledModelManager()

    def __unicode__(self):
        return unicode(self.hnscc_visit)

    def get_report_datetime(self):
        return self.hnscc_visit.report_datetime

    def get_subject_identifier(self):
        return self.hnscc_visit.get_subject_identifier()

    def get_visit(self):
        return self.hnscc_visit

    def natural_key(self):
        return self.hnscc_visit.natural_key()

    class Meta:
        abstract = True
