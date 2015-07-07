from edc.base.model.models import BaseUuidModel
from .hnscc_off_study_mixin import HnsccOffStudyMixin


class HnsccBaseUuidModel(HnsccOffStudyMixin, BaseUuidModel):

    """ Base model for all hnscc subject models """

    class Meta:
        abstract = True
