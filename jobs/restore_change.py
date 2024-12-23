import importlib

from django.contrib.contenttypes.models import ContentType
from django.db import models

from nautobot.extras.jobs import Job, register_job


class RestoreJob(Job):
    """
    Restore an entire change from the change log.
    """
    name = "Restoration Jobs"
    change_id = models.CharField(max_length=255)
    
    class Meta:
        name = "Restore from Change Log Job"
        description = "Restore an entire change from the change log."

    def run(self, *args, **kwargs):
        print("Restoring change...")

register_job(RestoreJob)
