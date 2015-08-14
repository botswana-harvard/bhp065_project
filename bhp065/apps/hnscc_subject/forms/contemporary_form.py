from .base_hnscc_model_form import BaseHnsccModelForm
from ..models import Contemporary


class ContemporaryForm (BaseHnsccModelForm):

    class Meta:
        model = Contemporary
