from nautobot.dcim.models import Device, Location, LocationType
from nautobot.extras.jobs import Job, FileVar, ChoiceVar
import csv
import io

class ImportWayneEnterprisesOnboardingData(Job):
    """Import Wayne Enterprises onboarding data from a CSV file."""
    
    csv_file = FileVar(
        label="CSV File",
        description="Upload a CSV file with the relevant information.",
        required=True,
    )
    import_type = ChoiceVar(
        label="Import Type",
        description="Select the type of import to perform.",
        required=True,
        choices=[("locations", "Locations")],
    )

    class Meta:
        name = "Import Wayne Enterprises Onboarding Data"
        description = "Import Wayne Enterprises onboarding data from a CSV file."

    def run(self, csv_file, **kwargs):
        csv_file_content = csv_file.read().decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(csv_file_content))

        if self.import_type == "locations":
            self.logger.info("Preparing to import locations from CSV file.")
            for row in csv_reader:
                try:
                    name_type_split = row["name"].split("-")
                    city = row["city"]
                    state = row["state"]
                except KeyError as err:
                    self.logger.error(f"Import file is missing a required column. {err}")
                    return                    

                if len(state) <=2:
                    self.logger.error(f"No state abbreviations allowed.  Please update {state} to use the full state name.")
                    continue

                try:
                    location_name = name_type_split[0]
                    location_type = name_type_split[1]
                except IndexError:
                    self.logger.error(f"Invalid location name format: {row['name']}.  Expected format is 'Location Name-Location Type'")
                    continue


                try:
                    location_type = LocationType.objects.get(name=location_type)
                except LocationType.DoesNotExist:
                    self.logger.error(f"Location type '{location_type}' does not exist.  Please create the location type before importing data.")
                    continue


                # try:
                #     location, created = Location.objects.get_or_create(name=location_name, location_type=location_type)
                # except Exception as err:
                #     self.logger.error(f"Error creating location: {err}")
                #     continue

        self.logger.info("Imported Wayne Enterprises onboarding data from CSV file.")
