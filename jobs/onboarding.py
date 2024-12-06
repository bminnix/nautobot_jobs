from nautobot.dcim.models import Device, Location, LocationType
from nautobot.extras.jobs import Job, FileVar
import csv
import io

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
        csv_file_content = csv_file.read().decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(csv_file_content))
        for row in csv_reader:
            print(row)

        self.logger.info("Imported Wayne Enterprises onboarding data from CSV file.")
