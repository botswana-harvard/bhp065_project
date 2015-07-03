from edc.base.form.forms import BaseModelForm
from ..models import Enrollment


class EnrollmentForm (BaseModelForm):

    class Meta:
        model = Enrollment
