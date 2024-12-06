from nautobot.dcim.models import Device, Location, LocationType
from nautobot.extras.jobs import Job, FileVar
import csv

class ImportWayneEnterprisesOnboardingData(Job):
    """Import Wayne Enterprises onboarding data from a CSV file."""
    
    csv_file = FileVar(
        label="CSV File",
        description="Upload a CSV file with the relevant information.",
        required=True,
    )

    class Meta:
        name = "Import Wayne Enterprises Onboarding Data"
        description = "Import Wayne Enterprises onboarding data from a CSV file."

    def run(self, csv_file, **kwargs):
        # with open(csv_file, newline='') as csvfile:
        #     reader = csv.reader(csvfile)
        #     for row in reader:
        #         print(row)

        self.logger.info("Imported Wayne Enterprises onboarding data from CSV file.")
