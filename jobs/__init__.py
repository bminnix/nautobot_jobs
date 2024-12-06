from nautobot.core.celery import register_jobs
from .onboarding import ImportWayneEnterprisesOnboardingData

jobs = [ImportWayneEnterprisesOnboardingData]

register_jobs(jobs)
