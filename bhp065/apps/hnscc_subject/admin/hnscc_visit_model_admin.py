from edc.base.modeladmin.admin import BaseModelAdmin
from ..models import HnsccVisit


class HnsccVisitModelAdmin (BaseModelAdmin):

    """Model Admin for models with a foreignkey to the hnscc_visit model."""

    visit_model = HnsccVisit
    visit_model_foreign_key = 'hnscc_visit'
    dashboard_type = 'subject'
