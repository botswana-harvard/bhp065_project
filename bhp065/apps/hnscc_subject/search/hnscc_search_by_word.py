from django.db.models import Q
from edc.dashboard.search.classes import BaseSearchByWord
from ..models import Enrollment


class HnsccSearchByWord(BaseSearchByWord):

    name = 'word'
    search_model = Enrollment
    order_by = ['-created']
    template = 'enrollment_include.html'

    @property
    def qset(self):
        qset = (
            Q(registered_subject__subject_identifier__icontains=self.search_value) |
            Q(pathology_no__icontains=self.search_value))
        return qset
