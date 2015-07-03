from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc.base.form.forms import BaseModelForm

from ..models.choices import OFF_STUDY_REASON
from ..models import HnsccVisit, HnsccOffStudy


class HnsccVisitVisitForm (BaseModelForm):

    reason = forms.ChoiceField(
        label='Reason for visit',
        choices=HnsccVisit().get_visit_reason_choices(),
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),)

    class Meta:
        model = HnsccVisit


class HnsccOffStudyOffStudyForm (BaseModelForm):

    reason = forms.ChoiceField(
        label='Please code the primary reason participant taken off-study',
        choices=[choice for choice in OFF_STUDY_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),)

    class Meta:
        model = HnsccOffStudy
