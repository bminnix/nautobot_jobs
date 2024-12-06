from nautobot.core.celery import register_jobs
from . import ImportWayneEnterprisesOnboardingData

jobs = [ImportWayneEnterprisesOnboardingData]

register_jobs(*jobs)
