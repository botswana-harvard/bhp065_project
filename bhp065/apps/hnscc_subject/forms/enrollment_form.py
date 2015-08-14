from django import forms

from edc.base.form.forms import BaseModelForm
from edc.constants import YES, NO

from ..models import Enrollment


class EnrollmentForm (BaseModelForm):

    def clean(self):

        cleaned_data = self.cleaned_data
        if cleaned_data.get('age') < 18:
            raise forms.ValidationError('Subject is TOO YOUNG and CANNOT be enrolled')
        if cleaned_data.get('age') > 130:
            raise forms.ValidationError('Subject is TOO OLD and CANNOT be enrolled')
        if cleaned_data.get('bpcc_enrolled') == YES and not cleaned_data.get('bid_number'):
            raise forms.ValidationError('Please provide the BID number if subject '
                                        'registered in BPCC/ BHP045')
        if cleaned_data.get('bpcc_enrolled') == NO and cleaned_data.get('bid_number'):
            raise forms.ValidationError('Subject is NOT enrolled in BPCC/BHP045. '
                                        'Do not provide BID number')
        cleaned_data = super(EnrollmentForm, self).clean()
        return cleaned_data

    class Meta:
        model = Enrollment
