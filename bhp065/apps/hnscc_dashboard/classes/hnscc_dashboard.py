from edc.dashboard.subject.classes import RegisteredSubjectDashboard

from apps.hnscc_subject.models import Enrollment, HnsccVisit


class HnsccDashboard(RegisteredSubjectDashboard):

    view = 'hnscc_dashboard'
    dashboard_url_name = 'hnscc_dashboard_url'
    dashboard_name = 'Hnscc Dashboard'
    urlpattern_view = 'apps.hnscc_dashboard.views'
    template_name = 'hnscc_dashboard.html'
    urlpatterns = [
        RegisteredSubjectDashboard.urlpatterns[0][:-1] + '(?P<appointment_code>{appointment_code})/$'
        ] + RegisteredSubjectDashboard.urlpatterns
    urlpattern_options = dict(
        RegisteredSubjectDashboard.urlpattern_options,
        dashboard_model=RegisteredSubjectDashboard.urlpattern_options['dashboard_model'] + '|enrollment',
        dashboard_type='subject',
        appointment_code='1000')

    def __init__(self, *args, **kwargs):
        super(HnsccDashboard, self).__init__(*args, **kwargs)
        self.visit_model = HnsccVisit
        self.subject_dashboard_url = 'hnscc_dashboard_url'
        self.membership_form_category = ['subject_enrollment']
        self.dashboard_type_list = ['subject']
        self.dashboard_models['enrollment'] = Enrollment
        self.dashboard_models['visit'] = self._visit_model

    def get_context_data(self, **kwargs):
        super(HnsccDashboard, self).get_context_data(**kwargs)
        self.context.update(
            home='hnscc',
            search_name='subject',
            subject_dashboard_url=self.subject_dashboard_url,
            title='Hnscc Dashboard',
            hiv_status=self.hnscc_hiv_status(),
            smoking_status=self.hnscc_smoking_status(),
            )
        return self.context

    def set_dashboard_type_list(self):
        self._dashboard_type_list = ['subject']

    def get_subject_identifier(self):
        return self.subject_identifier

    def get_visit_model(self):
        return HnsccVisit

    def hnscc_hiv_status(self):
        st = Enrollment.objects.filter(registered_subject=self.registered_subject)
        if st:
            if st[0].hiv_status == 'INFECTED':
                self._hnscc_hiv_status = 'HIV Infected'
            elif st[0].hiv_status == 'UNINFECTED':
                self._hnscc_hiv_status = 'HIV uninfected'
            elif not self._hnscc_hiv_status:
                self._hnscc_hiv_status = 'UNK'
            return self._hnscc_hiv_status

    def hnscc_smoking_status(self):
        st = Enrollment.objects.filter(registered_subject=self.registered_subject)
        if st:
            if st[0].smoking_status == 'smoker':
                self._hnscc_smoking_status = 'smoker'
            elif st[0].smoking_status == 'non-smoker':
                self._hnscc_smoking_status = 'non-smoker'
            elif not self._hnscc_smoking_status:
                self._hnscc_smoking_status = 'UNK'
            return self._hnscc_smoking_status
