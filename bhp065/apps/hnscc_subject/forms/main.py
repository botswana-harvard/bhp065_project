from edc.base.form.forms import BaseModelForm

from ..models import HnsccVisit, HnsccOffStudy


class HnsccVisitForm (BaseModelForm):

    class Meta:
        model = HnsccVisit


class HnsccOffStudyForm (BaseModelForm):

    class Meta:
        model = HnsccOffStudy
