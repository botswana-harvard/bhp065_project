import factory
from datetime import datetime

from edc.core.identifier.classes import SubjectIdentifier
from edc.subject.registration.models import RegisteredSubject
from ...models import Enrollment


class EnrolledSubjectFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Enrollment

    report_datetime = datetime.today()
    gender = 'F'
    age = 26
    hiv_status = 'INFECTED'
    smoking_status = 'non-smoker'
    registered_subject = RegisteredSubject.objects.create(
        first_name='Anonymous',
        subject_type='subject',
        subject_identifier=SubjectIdentifier(site_code='040').get_identifier(),
        registration_status='enrolled')
