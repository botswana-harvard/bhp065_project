from collections import OrderedDict

from edc.subject.visit_schedule.classes import (VisitScheduleConfiguration, site_visit_schedules,
                                                EntryTuple, MembershipFormTuple,
                                                ScheduleGroupTuple, RequisitionPanelTuple)
from edc.constants import REQUIRED, NOT_ADDITIONAL, NOT_REQUIRED, ADDITIONAL

from ..models import Enrollment, HnsccVisit


class HnsccVisitSchedule(VisitScheduleConfiguration):

    name = 'head and neck visit schedule'
    app_label = 'hnscc_subject'
    membership_forms = OrderedDict({
        'subject_enrollment': MembershipFormTuple('subject_enrollment',
                                                  Enrollment, True), })
    schedule_groups = OrderedDict({
        'Subject Enrollment': ScheduleGroupTuple('Subject Enrollment', 'subject_enrollment',
                                                 None, None), })
    visit_definitions = OrderedDict()
    visit_definitions['1000'] = {
        'title': 'Enrollment Visit',
        'time_point': 0,
        'base_interval': 0,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 45,
        'window_upper_bound_unit': 'D',
        'grouping': None,
        'visit_tracking_model': HnsccVisit,
        'schedule_group': 'Subject Enrollment',
        'instructions': None,
        'requisitions': (
            RequisitionPanelTuple(10L, u'hnscc_lab', u'hnsccrequisition', 'HPV Testing',
                                  'TEST', 'WB', NOT_REQUIRED, NOT_ADDITIONAL), ),
        'entries': (
            EntryTuple(10L, u'hnscc_subject', u'contemporary', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(20L, u'hnscc_subject', u'historical', REQUIRED, NOT_ADDITIONAL),
            EntryTuple(1010L, u'hnscc_subject', u'hnsccoffstudy', NOT_REQUIRED, ADDITIONAL),)}
site_visit_schedules.register(HnsccVisitSchedule)
