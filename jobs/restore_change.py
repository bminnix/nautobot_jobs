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
    change_id = StringVar(description="The ID of the change to restore.")
    

    class Meta:
        name = "Restore from Change Log Job"
        description = "Restore an entire change from the change log."
        

    def run(self, change_id):
        print(f"Restoring change {change_id}...")

register_jobs(RestoreJob)
