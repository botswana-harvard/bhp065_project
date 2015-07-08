from edc.lab.lab_profile.classes import site_lab_profiles

from edc.lab.lab_profile.classes import LabProfile

from .models import (Aliquot, AliquotType, Receive, HnsccRequisition,
                     AliquotProfile, AliquotProfileItem, Panel)


class BaseHnsccProfile(LabProfile):
    aliquot_model = Aliquot
    aliquot_type_model = AliquotType
    profile_model = AliquotProfile
    profile_item_model = AliquotProfileItem
    receive_model = Receive
    panel_model = Panel


class HnsccSubjectProfile(BaseHnsccProfile):
    requisition_model = HnsccRequisition
    name = HnsccRequisition._meta.object_name
site_lab_profiles.register(HnsccSubjectProfile)
