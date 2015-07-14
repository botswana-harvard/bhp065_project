from django import forms
from edc.base.form.forms import BaseModelForm
from ..models import Enrollment


class EnrollmentForm (BaseModelForm):

    def clean(self):

        cleaned_data = self.cleaned_data
        if cleaned_data.get('age') < 18:
            raise forms.ValidationError('Subject is TOO YOUNG and CANNOT be enrolled')
        if cleaned_data.get('age') > 130:
            raise forms.ValidationError('Subject is TOO OLD and CANNOT be enrolled')
        cleaned_data = super(EnrollmentForm, self).clean()
        return cleaned_data

    class Meta:
        model = Enrollment
