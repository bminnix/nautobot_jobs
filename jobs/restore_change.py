import importlib

from django.contrib.contenttypes.models import ContentType
from django.db import models

from nautobot.apps.jobs import register_jobs
from nautobot.extras.jobs import Job


class RestoreJob(Job):
    """
    Restore an entire change from the change log.
    """
    name = "Restoration Jobs"
    
    class Meta:
        name = "Restore from Change Log Job"
        description = "Restore an entire change from the change log."
        change_id = models.CharField(max_length=255)

    def run(self, *args, **kwargs):
        print("Restoring change...")

register_jobs(RestoreJob)
