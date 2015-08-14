from datetime import datetime, date

from edc.apps.app_configuration.classes import BaseAppConfiguration
from edc.core.bhp_variables.models import StudySpecific, StudySite
from edc.device.device.classes import device
from edc.lab.lab_profile.classes import ProfileItemTuple, ProfileTuple
from lis.specimen.lab_aliquot_list.classes import AliquotTypeTuple
from lis.specimen.lab_panel.classes import PanelTuple
from lis.labeling.classes import LabelPrinterTuple, ZplTemplateTuple, ClientTuple

study_start_datetime = datetime(2015, 07, 01, 7, 30, 00)
study_end_datetime = datetime(2020, 06, 30, 7, 30, 00)

try:
    from config.labels import aliquot_label
except ImportError:
    aliquot_label = None


class HnsccAppConfiguration(BaseAppConfiguration):

    def prepare(self):
        super(HnsccAppConfiguration, self).prepare()

    global_configuration = {
        'dashboard':
            {'show_not_required_metadata': False,
             'allow_additional_requisitions': False,
             'show_drop_down_requisitions': True},
        'appointment':
            {'allowed_iso_weekdays': '12345',
             'use_same_weekday': True,
             'default_appt_type': 'default'}, }

    study_variables_setup = {
        'protocol_number': 'BHP000',
        'protocol_code': '000',
        'protocol_title': 'BHP000',
        'research_title': 'BHP000',
        'study_start_datetime': study_start_datetime,
        'minimum_age_of_consent': 18,
        'maximum_age_of_consent': 130,
        'gender_of_consent': 'MF',
        'subject_identifier_seed': '10000',
        'subject_identifier_prefix': '000',
        'subject_identifier_modulus': '7',
        'subject_type': 'subject',
        'machine_type': 'SERVER',
        'hostname_prefix': '0000',
        'device_id': device.device_id}

    holidays_setup = {
        'New Year': date(2015, 1, 01),
        'New Year Holiday': date(2015, 1, 02),
        'Good Fiday': date(2015, 4, 3),
        'Easter Monday': date(2015, 4, 6),
        'Labour Day': date(2015, 5, 1),
        'Ascension Day': date(2015, 5, 14),
        'Sir Seretse Khama Day': date(2015, 7, 01),
        'President\'s Day': date(2015, 7, 20),
        'President\'s Day Holiday': date(2015, 7, 21),
        'Independence Day': date(2015, 9, 30),
        'Botswana Day Holiday': date(2015, 10, 01),
        'Christmas Day': date(2015, 12, 25),
        'Boxing Day': date(2015, 12, 26), }

    consent_catalogue_setup = {
        'name': 'hnscc',
        'content_type_map': 'enrollment',
        'consent_type': 'study',
        'version': 1,
        'start_datetime': study_start_datetime,
        'end_datetime': study_end_datetime,
        'add_for_app': 'hnscc_subject'}

    study_site_setup = [{'site_name': 'site1', 'site_code': '001'},
                        {'site_name': 'site2', 'site_code': '002'}, ]

    consent_catalogue_list = [consent_catalogue_setup]
#
#     lab_clinic_api_setup = {
#         'panel': [],
#         'aliquot_type': []}
#
#     lab_setup = {'hnscc': {
#                     'panel': [],
#                     'aliquot_type': [],
#                      'profile': [],
#                      'profile_item': []}}

    lab_clinic_api_setup = {
        'panel': [PanelTuple('HPV Testing', 'TEST', 'WB')],
        'aliquot_type': [AliquotTypeTuple('Whole Blood', 'WB', '02')]}

    lab_setup = {
        'hnscc': {
            'panel': [PanelTuple('HPV Testing', 'TEST', 'WB')],
            'aliquot_type': [AliquotTypeTuple('Whole Blood', 'WB', '02'),
                             AliquotTypeTuple('HPV Testing', 'HPV', '803')],
            'profile': [ProfileTuple('HPV Testing', 'WB')],
            'profile_item': [ProfileItemTuple('HPV Testing', 'HPV', 1.0, 1), ]}}

    labeling_setup = {
        'label_printer': [LabelPrinterTuple
                          ('Zebra_Technologies_ZTC_GK420t', 'hostname', 'localhost', False), ],
        'client': [ClientTuple(hostname='hostname',
                               printer_name='Zebra_Technologies_ZTC_GK420t',
                               cups_hostname='hostname',
                               ip=None,
                               aliases=None), ],
        'zpl_template': [
            aliquot_label or ZplTemplateTuple(
                'aliquot_label', (
                    ('^XA\n'
                     '^FO300,15^A0N,20,20^FD${protocol} Site ${site} ${clinician_initials}   '
                     '${aliquot_type} ${aliquot_count}${primary}^FS\n'
                     '^FO300,34^BY1,3.0^BCN,50,N,N,N\n'
                     '^BY^FD${aliquot_identifier}^FS\n'
                     '^FO300,92^A0N,20,20^FD${aliquot_identifier}^FS\n'
                     '^FO300,112^A0N,20,20^FD${subject_identifier} (${initials})^FS\n'
                     '^FO300,132^A0N,20,20^FDDOB: ${dob} ${gender}^FS\n'
                     '^FO300,152^A0N,25,20^FD${drawn_datetime}^FS\n'
                     '^XZ')), True),
            ZplTemplateTuple(
                'requisition_label', (
                    ('^XA\n'
                     '^FO300,15^A0N,20,20^FD${protocol} Site ${site} ${clinician_initials}   '
                     '${aliquot_type} ${aliquot_count}${primary}^FS\n'
                     '^FO300,34^BY1,3.0^BCN,50,N,N,N\n'
                     '^BY^FD${requisition_identifier}^FS\n'
                     '^FO300,92^A0N,20,20^FD${requisition_identifier} ${panel}^FS\n'
                     '^FO300,112^A0N,20,20^FD${subject_identifier} (${initials})^FS\n'
                     '^FO300,132^A0N,20,20^FDDOB: ${dob} ${gender}^FS\n'
                     '^FO300,152^A0N,25,20^FD${drawn_datetime}^FS\n'
                     '^XZ')), False), ]}

    def update_or_create_study_variables(self):
        if StudySpecific.objects.all().count() == 0:
            StudySpecific.objects.create(**self.study_variables_setup)
        else:
            StudySpecific.objects.all().update(**self.study_variables_setup)
        self._setup_study_sites()

    def _setup_study_sites(self):
        for site in self.study_site_setup:
            try:
                StudySite.objects.get(**site)
            except StudySite.DoesNotExist:
                StudySite.objects.create(**site)

hnscc_app_configuration = HnsccAppConfiguration()
