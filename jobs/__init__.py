from nautobot.core.celery import register_jobs
from .onboarding import ImportWayneEnterprisesOnboardingData

register_jobs(ImportWayneEnterprisesOnboardingData)
