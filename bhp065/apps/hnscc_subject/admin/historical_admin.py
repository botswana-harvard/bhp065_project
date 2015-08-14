from django.contrib import admin
from .hnscc_visit_model_admin import HnsccVisitModelAdmin
from ..models import Historical
from ..forms import HistoricalForm


class HistoricalAdmin(HnsccVisitModelAdmin):

    form = HistoricalForm
    fields = (
        "hnscc_visit",
        "serial",
        "received",
        "histo_no",
        "pathology_no",
        "hospital",
        "specimen_size",
        "nature_of_specimen",
        "tissues",
        "clinical_dx",
        "final_dx",
        "diagnosis_date",
        "topography_code",
        "morphology_code",
        "no_of_blocks")
    radio_fields = {
        "hospital": admin.VERTICAL, }
admin.site.register(Historical, HistoricalAdmin)
