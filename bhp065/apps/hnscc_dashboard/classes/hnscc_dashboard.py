from edc.dashboard.subject.classes import RegisteredSubjectDashboard

from apps.hnscc_subject.models import Enrollment, HnsccVisit
from apps.hnscc_lab.models import HnsccRequisition
from edc.constants import YES, NO

class HnsccDashboard(RegisteredSubjectDashboard):

    view = 'hnscc_dashboard'
    dashboard_url_name = 'hnscc_dashboard_url'
    dashboard_name = 'Hnscc Dashboard'
    urlpattern_view = 'apps.hnscc_dashboard.views'
    template_name = 'hnscc_dashboard.html'
    urlpatterns = [
        RegisteredSubjectDashboard.urlpatterns[0][:-1] +
        '(?P<appointment_code>{appointment_code})/$'] + RegisteredSubjectDashboard.urlpatterns
    urlpattern_options = dict(
        RegisteredSubjectDashboard.urlpattern_options,
        dashboard_model=RegisteredSubjectDashboard.urlpattern_options['dashboard_model'] + '|enrollment',
        dashboard_type='subject',
        appointment_code='1000')

    def __init__(self, *args, **kwargs):
        super(HnsccDashboard, self).__init__(*args, **kwargs)
        self.subject_dashboard_url = 'hnscc_dashboard_url'
        self.membership_form_category = ['subject_enrollment']
        self.dashboard_type_list = ['subject']
        self.visit_model = HnsccVisit
        self._visit_model = HnsccVisit
        self._locator_model = None
        self.requisition_model = HnsccRequisition
        self.dashboard_models['enrollment'] = Enrollment

    def get_context_data(self, **kwargs):
        super(HnsccDashboard, self).get_context_data(**kwargs)
        self.context.update(
            home='hnscc',
            search_name='subject',
            subject_dashboard_url=self.subject_dashboard_url,
            title='Hnscc Dashboard',
            hiv_status=self.hnscc_hiv_status(),
            smoking_status=self.hnscc_smoking_status(),
            enrollment=self.enrollment(),
            bpcc_enrollment=self.is_bpcc_enrolled(), )
        return self.context

    def set_dashboard_type_list(self):
        self._dashboard_type_list = ['subject']

    def get_subject_identifier(self):
        return self.subject_identifier

    def get_visit_model(self):
        return HnsccVisit

    def enrollment(self):
        try:
            enrollment = Enrollment.objects.get(registered_subject=self.registered_subject)
        except Enrollment.DoesNotExist:
            enrollment = None
        return enrollment

    def hnscc_hiv_status(self):
        st = Enrollment.objects.filter(registered_subject=self.registered_subject)
        if st:
            if st[0].hiv_status == 'INFECTED':
                self._hnscc_hiv_status = 'HIV Infected'
            elif st[0].hiv_status == 'UNINFECTED':
                self._hnscc_hiv_status = 'HIV uninfected'
            elif st[0]._hnscc_hiv_status == 'UNK':
                self._hnscc_hiv_status = 'UNK'
            return self._hnscc_hiv_status

    def hnscc_smoking_status(self):
        st = Enrollment.objects.filter(registered_subject=self.registered_subject)
        if st:
            if st[0].smoking_status == 'smoker':
                self._hnscc_smoking_status = 'smoker'
            elif st[0].smoking_status == 'non-smoker':
                self._hnscc_smoking_status = 'non-smoker'
            elif st[0].smoking_status == 'UNK':
                self._hnscc_smoking_status = 'Unknown'
            return self._hnscc_smoking_status

    def is_bpcc_enrolled(self):
        st = Enrollment.objects.filter(registered_subject=self.registered_subject)
        if st:
            if st[0].bpcc_enrolled == YES:
                self._get_bpcc_bid = 'ENROLLED'
            elif st[0].bpcc_enrolled == NO:
                self._get_bpcc_bid = 'NOT ENROLLED'
            return self._get_bpcc_bid

    @property
    def registered_subject(self):
        enroll = None
        try:
            enroll = Enrollment.objects.get(id=self.dashboard_id)
        except Enrollment.DoesNotExist:
            visit = None
            try:
                visit = HnsccVisit.objects.get(id=self.dashboard_id)
            except HnsccVisit.DoesNotExist:
                pass
        return enroll.registered_subject if enroll else visit.appointment.registered_subject if visit else None
