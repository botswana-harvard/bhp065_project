from datetime import datetime

from edc.subject.visit_tracking.tests.factories import BaseVisitTrackingFactory
from ...models import HnsccVisit


class HnsccVisitFactory(BaseVisitTrackingFactory):
    FACTORY_FOR = HnsccVisit

    report_datetime = datetime.today()
    data_type = 'contemporary'
    reason = 'UNSCHEDULED'
