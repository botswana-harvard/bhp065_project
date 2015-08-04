from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc.lab.lab_requisition.forms import BaseRequisitionForm

from ..models import HnsccRequisition
from apps.hnscc_subject.models.choices import REASON_NOT_DRAWN


class HnsccRequisitionForm(BaseRequisitionForm):

    reason_not_drawn = forms.ChoiceField(
        label='If not drawn, please explain',
        choices=[choice for choice in REASON_NOT_DRAWN],
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer), )

    def __init__(self, *args, **kwargs):

        super(HnsccRequisitionForm, self).__init__(*args, **kwargs)

        self.fields['item_type'].initial = 'tube'

    def clean(self):
        super(HnsccRequisitionForm, self).clean()

        cleaned_data = self.cleaned_data

        return cleaned_data

    class Meta:
        model = HnsccRequisition
