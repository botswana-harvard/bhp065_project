from edc.lab.lab_requisition.forms import BaseRequisitionForm

from ..models import HnsccRequisition


class HnsccRequisitionForm(BaseRequisitionForm):

    def __init__(self, *args, **kwargs):

        super(HnsccRequisitionForm, self).__init__(*args, **kwargs)

        self.fields['item_type'].initial = 'tube'

    def clean(self):
        super(HnsccRequisitionForm, self).clean()

        cleaned_data = self.cleaned_data

        return cleaned_data

    class Meta:
        model = HnsccRequisition
