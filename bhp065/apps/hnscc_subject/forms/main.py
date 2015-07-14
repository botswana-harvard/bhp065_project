from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
from edc.base.form.forms import BaseModelForm
from edc.subject.off_study.forms import BaseOffStudyForm

from ..models import HnsccVisit, HnsccOffStudy
from ..models.choices import OFF_STUDY_REASON


class HnsccVisitForm (BaseModelForm):

    reason = forms.ChoiceField(
        label='Reason for visit',
        choices=HnsccVisit().get_visit_reason_choices(),
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer), )

    class Meta:
        model = HnsccVisit


class HnsccOffStudyForm (BaseOffStudyForm):

    reason = forms.ChoiceField(
        label='Reason for off-study',
        choices=[choice for choice in OFF_STUDY_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),)

    class Meta:
        model = HnsccOffStudy
