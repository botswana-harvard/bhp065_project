from django.db import models

from edc.lab.lab_profile.models import BaseProcessing

from .aliquot import Aliquot
from .aliquot_profile import AliquotProfile
from ..managers import AliquotProcessingManager


class AliquotProcessing(BaseProcessing):

    aliquot = models.ForeignKey(
        Aliquot,
        verbose_name='Source Aliquot',
        help_text='Create aliquots from this one.')

    profile = models.ForeignKey(
        AliquotProfile,
        verbose_name='Profile',
        help_text='Create aliquots according to this profile.')

    objects = AliquotProcessingManager()

    def natural_key(self):
        return self.aliquot.natural_key() + self.profile.natural_key()

    def deserialize_get_missing_fk(self, attrname):
        retval = None
        return retval

    class Meta:
        app_label = 'hnscc_lab'
        db_table = 'hnscc_lab_processing'
