from django import forms
from django.core.exceptions import ValidationError
from django.test.testcases import TestCase

from edc.subject.registration.models import RegisteredSubject
from ...hnscc_subject.models import Enrollment
from ..forms import EnrollmentForm
from .factories import EnrolledSubjectFactory


class TestEnrolledSubject(TestCase):

    def setUp(self):
        self.enrollment = EnrolledSubjectFactory()

    def test_enrollment(self):
        print """Test Enrolling a subject"""
        print "Enrolled Subject: {}".format(self.enrollment)
        print "assert there is one enrolled subject saved"
        self.assertEqual(Enrollment.objects.all().count(), 1)

        print 'get enrollment registered subject'
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=self.enrollment.registered_subject.subject_identifier)
        print registered_subject
        print "assert registered subject was created and updated successfully for the enrollment"
        self.assertEqual(registered_subject, self.enrollment.registered_subject)

    def enrollment_age(self):
        print "Enrolling an underage subject"
        age = EnrollmentForm()
        age.cleaned_data = {'age': 12}
        print "assert subject is not enrolled"
        self.assertRaisesMessage(ValidationError, 'Subject is TOO YOUNG and CANNOT be enrolled', age.clean)
