from django.test.testcases import TestCase
from edc.subject.appointment.models import Appointment
from edc.subject.registration.models import RegisteredSubject
from ...hnscc_subject.models import Enrollment
from .factories import EnrolledSubjectFactory


class TestEnrolledSubject(TestCase):

    def setUp(self):
        pass

    def test_enrollment(self):

        print """Test Enrolling a subject"""
        enrolled_subject = EnrolledSubjectFactory()
        print "Enrolled Subject: {}".format(enrolled_subject)
        print "assert there is one enrolled subject saved"
        self.assertEqual(Enrollment.objects.all().count(), 1)

        print 'get enrollment registered subject'
        registered_subject = RegisteredSubject.objects.get(subject_identifier=enrolled_subject.registered_subject.subject_identifier)
        print registered_subject
        print "assert registered subject was created and updated successfully for the enrollment"
        self.assertEqual(registered_subject, enrolled_subject.registered_subject)
