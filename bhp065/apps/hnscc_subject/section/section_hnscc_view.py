from edc.dashboard.section.classes import BaseSectionView, site_sections

from ..search import HnsccSearchByWord
from ..models import Enrollment


class SectionHnsccView(BaseSectionView):
    section_name = 'subject'
    section_display_name = 'Subjects'
    section_display_index = 10
    section_template = 'section_hnscc_subject.html'
    dashboard_url_name = 'hnscc_dashboard_url'
    add_model = Enrollment
    search = {'word': HnsccSearchByWord}
    show_most_recent = True

site_sections.register(SectionHnsccView)
