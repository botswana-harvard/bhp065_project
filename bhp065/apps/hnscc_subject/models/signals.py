from django.db.models.signals import post_save
from django.dispatch import receiver

from .enrollment import Enrollment


@receiver(post_save, weak=False, dispatch_uid='query_bpcc_cohort')
def query_bpcc_cohort(sender, instance, raw, created, using, **kwarg):
    if isinstance(instance, Enrollment):
        instance.query_bpcc_cohort()
