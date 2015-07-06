from edc.dashboard.search.classes import BaseSearchByWord
from ..models import Enrollment


class HnsccSearchByWord(BaseSearchByWord):

    name = 'word'
    search_model = Enrollment
    order_by = ['-created']
    template = 'enrollment_include.html'
