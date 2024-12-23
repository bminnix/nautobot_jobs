import importlib

from django.contrib.contenttypes.models import ContentType

from nautobot.apps.jobs import register_jobs
from nautobot.extras.jobs import Job, StringVar
# from nautobot.extras.jobs import BooleanVar, ChoiceVar, FileVar, Job, ObjectVar, RunJobTaskFailed, StringVar, TextVar


class RestoreJob(Job):
    """
    Restore an entire change from the change log.
    """
    name = "Restoration Jobs"
    change_id = (max_length=255)
    
    class Meta:
        name = "Restore from Change Log Job"
        description = "Restore an entire change from the change log."
        

    def run(self, *args, **kwargs):
        print("Restoring change...")

register_jobs(RestoreJob)
