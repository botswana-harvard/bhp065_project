from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.subject.lab_tracker.classes import HivLabTracker


class HnsccHivLabTracker(HivLabTracker):
    subject_type = 'subject'
    trackers = []

site_lab_tracker.register(HnsccHivLabTracker)
