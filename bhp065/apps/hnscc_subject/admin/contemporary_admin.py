from django.contrib import admin
from .hnscc_visit_model_admin import HnsccVisitModelAdmin
from ..models import Contemporary
from ..forms import ContemporaryForm


class ContemporaryAdmin(HnsccVisitModelAdmin):

    form = ContemporaryForm
    fields = (
        "hnscc_visit",
        "pathology_no",
        "diagnosis_date",
        "specimen_collecton",
        "specimen_size",
        "nature_of_specimen",
        "specimen_size",
        "nature_of_specimen",
        "tissues",
        "topography_code",
        "morphology_code",
        "diagnosis",
        "bpcc_enrolled",
        "bid_number",
        "any_duplications")
    radio_fields = {
        "bpcc_enrolled": admin.VERTICAL,
        "any_duplications": admin.VERTICAL, }
admin.site.register(Contemporary, ContemporaryAdmin)
