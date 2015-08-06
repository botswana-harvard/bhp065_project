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
            'pathology_no',
            'gender',
            'age',
            'hiv_status',
            'smoking_status',
            "bpcc_enrolled",
            "bid_number", ]
        self.list_display = ("registered_subject", "pathology_no", "gender", "age",
                             "bpcc_enrolled", "bid_number")
        self.radio_fields = {'gender': admin.VERTICAL,
                             'hiv_status': admin.VERTICAL,
                             'smoking_status': admin.VERTICAL,
                             "bpcc_enrolled": admin.VERTICAL, }
        self.list_filter = ('gender', "bpcc_enrolled", "report_datetime")
admin.site.register(Enrollment, EnrollmentAdmin)
