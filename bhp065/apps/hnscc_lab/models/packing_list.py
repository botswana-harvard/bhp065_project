from django.db import models

from edc.lab.lab_packing.models import BasePackingList

from ..managers import PackingListManager
from .hnscc_requisition import HnsccRequisition
from .aliquot import Aliquot


class PackingList(BasePackingList):

    objects = PackingListManager()

    def natural_key(self):
        return (self.timestamp, )

    @property
    def item_models(self):
        return[HnsccRequisition, Aliquot]

    @property
    def packing_list_item_model(self):
        return models.get_model('hnscc_lab', 'PackingListItem')

    class Meta:
        app_label = "hnscc_lab"
        verbose_name = 'Packing List'
