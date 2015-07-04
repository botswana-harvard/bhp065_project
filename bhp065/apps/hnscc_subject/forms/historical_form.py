from .base_hnscc_model_form import BaseHnsccModelForm
from ..models import Historical


class HistoricalForm (BaseHnsccModelForm):

    class Meta:
        model = Historical
