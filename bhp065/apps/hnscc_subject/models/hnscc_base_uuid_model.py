from edc.device.sync.models import BaseSyncUuidModel
from .hnscc_off_study_mixin import HnsccOffStudyMixin


class HnsccBaseUuidModel(HnsccOffStudyMixin, BaseSyncUuidModel):

    """ Base model for all hnscc subject models """

    class Meta:
        abstract = True
