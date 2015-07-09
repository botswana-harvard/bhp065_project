from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin

from ..forms import EnrollmentForm
from ..models import Enrollment


class EnrollmentAdmin(BaseModelAdmin):

    dashboard_type = 'subject'
    form = EnrollmentForm

    def __init__(self, *args, **kwargs):
        super(EnrollmentAdmin, self).__init__(*args, **kwargs)
        self.fields = [
            'report_datetime',
            'gender',
            'age',
            'hiv_status',
            'smoking_status',
            'survival_status', ]
        self.radio_fields = {'gender': admin.VERTICAL,
                             'hiv_status': admin.VERTICAL,
                             'smoking_status': admin.VERTICAL,
                             'survival_status': admin.VERTICAL, }
admin.site.register(Enrollment, EnrollmentAdmin)
