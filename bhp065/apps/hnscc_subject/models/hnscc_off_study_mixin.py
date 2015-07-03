from edc.subject.off_study.mixins.off_study_mixin import OffStudyMixin


class HnsccOffStudyMixin(OffStudyMixin):

    def get_off_study_cls(self):
        from .hnscc_off_study import HnsccOffStudy
        return HnsccOffStudy
