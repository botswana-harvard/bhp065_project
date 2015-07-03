from django.contrib import admin

from edc.subject.consent.admin import BaseConsentModelAdmin

from ..forms import EnrollmentForm
from ..models import Enrollment


class EnrollmentAdmin(BaseConsentModelAdmin):

    dashboard_type = 'subject'
    form = EnrollmentForm

    def __init__(self, *args, **kwargs):
        super(EnrollmentAdmin, self).__init__(*args, **kwargs)
        self.fields = [
            'registered_subject',
            'subject_identifier',
            'report_datetime',
            'gender',
            'age',
            'hiv_status',
            'smoking_status']
        self.radio_fields({'hiv_status': admin.VERTICAL,
                           'smoking_status': admin.VERTICAL,
                           })
admin.site.register(Enrollment, EnrollmentAdmin)
