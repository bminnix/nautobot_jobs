from nautobot.apps.jobs import register_jobs
from .onboarding import ImportWayneEnterprisesOnboardingData

jobs = [ImportWayneEnterprisesOnboardingData]

register_jobs(*jobs)
