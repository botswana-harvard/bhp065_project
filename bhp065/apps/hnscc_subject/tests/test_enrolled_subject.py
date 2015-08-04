from django import forms
from django.core.exceptions import ValidationError
from django.test.testcases import TestCase


from edc.entry_meta_data.models import ScheduledEntryMetaData
from edc.lab.lab_profile.classes import site_lab_profiles
from edc.lab.lab_profile.exceptions import AlreadyRegistered
from edc.subject.entry.models import Entry
from edc.subject.visit_schedule.classes import site_visit_schedules
from edc.subject.lab_tracker.classes import site_lab_tracker
from ...hnscc.app_configuration.classes import HnsccAppConfiguration
from ...hnscc_lab.lab_profiles import HnsccSubjectProfile

from edc.subject.appointment.models import Appointment
from edc.subject.registration.models import RegisteredSubject
from ...hnscc_subject.models import Enrollment, HnsccVisit
from ..forms import EnrollmentForm
from .factories import EnrolledSubjectFactory, HnsccVisitFactory


class TestEnrolledSubject(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(HnsccSubjectProfile())
        except AlreadyRegistered:
            pass
        HnsccAppConfiguration().prepare()
        site_lab_tracker.autodiscover()
        site_visit_schedules.autodiscover()
        site_visit_schedules.build_all()
        print "assert appointment is created for enrolled subject"
        self.enrolled_subject = EnrolledSubjectFactory()
        self.appointment = Appointment.objects.get(registered_subject=self.enrolled_subject.registered_subject)

    def test_enrollment(self):
        print """Test Enrolling a subject"""
        print "Enrolled Subject: {}".format(self.enrolled_subject)
        print "assert there is one enrolled subject saved"
        self.assertEqual(Enrollment.objects.all().count(), 1)

        print 'get enrollment registered subject'
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=self.enrolled_subject.registered_subject.subject_identifier)
        print registered_subject
        print "assert registered subject was created and updated successfully for the enrollment"
        self.assertEqual(registered_subject, self.enrolled_subject.registered_subject)

    def enrollment_under_age(self):
        print "Enrolling an underage subject"
        age = EnrollmentForm()
        age.cleaned_data = {'age': 12}
        print "assert under-age subject is not enrolled"
        self.assertRaisesMessage(ValidationError, 'Subject is TOO YOUNG and CANNOT be enrolled', age.clean)

    def enrollment_over_age(self):
        print "Enrolling an overage subject"
        age_max = EnrollmentForm()
        print "assert over-age subject is not enrolled"
        age_max.cleaned_data = {'age': 140}
        self.assertRaisesMessage(ValidationError, 'Subject is TOO OLD and CANNOT be enrolled', age_max.clean)

    def enrolled_subject_appointment(self):
        print "Checking created appointment"
        print "assert there is only one appointment"
        self.assertEqual(Appointment.objects.all().count(), 1)
        print "assert this is the 1000 visit"
        self.assertEqual(self.appointment.visit_definition.code, '1000')

    def visit_for_enrolled_subject(self):
        print "assert a visit is available"
        HnsccVisitFactory(appointment=self.appointment)
        self.assertEqual(HnsccVisit.objects.all().count(), 1)

    def contemporary_visit_meta_data(self):
        HnsccVisitFactory(appointment=self.appointment)
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=self.enrolled_subject.registered_subject.subject_identifier)
        entry = Entry.objects.get(model_name='contemporary',
            visit_definition_id=self.appointment.visit_definition_id)
        meta_data = ScheduledEntryMetaData.objects.get(appointment=self.appointment,
            registered_subject=registered_subject, entry=entry)
        self.assertEqual(meta_data.entry_status, 'NEW')

#     def historical_visit_meta_data(self):
#         HnsccVisitFactory(appointment=self.appointment, data_type='historical')
#         registered_subject = RegisteredSubject.objects.get(
#             subject_identifier=self.enrolled_subject.registered_subject.subject_identifier)
#         entry = Entry.objects.get(model_name='historical',
#             visit_definition_id=self.appointment.visit_definition_id)
#         meta_data = ScheduledEntryMetaData.objects.get(appointment=self.appointment,
#             registered_subject=registered_subject, entry=entry)
#         self.assertEqual(meta_data.entry_status, 'NEW')
