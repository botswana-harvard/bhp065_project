from edc.subject.off_study.admin import BaseOffStudyModelAdmin


class HnsccOffStudyModelAdmin (BaseOffStudyModelAdmin):

    dashboard_type = 'subject'
    visit_model_name = 'hnsccvisit'
