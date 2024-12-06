from nautobot.dcim.models import Device, Location, LocationType
from nautobot.extras.jobs import Job, FileVar, ChoiceVar
from nautobot.extras.models import Status
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

    def run(self, csv_file, import_type, **kwargs):
        location_types = {"BR": "Branch", "DC": "Data Center"}
        csv_file_content = csv_file.read().decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(csv_file_content))
        active_status = Status.objects.get(name="Active")

        if import_type == "locations":
            self.logger.info("Preparing to import locations from CSV file.")
            for row in csv_reader:
                try:
                    # Extract the required keyed values from the row
                    name_type_split = row["name"].split("-")
                    city = row["city"]
                    state = row["state"]
                    self.logger.info(f"Processing {name_type_split[0]} - {name_type_split[1]} for {city}, {state}")
                except KeyError as err:
                    self.logger.error(f"Import file is missing a required column. {err}")
                    return                    

                if len(state) <=2:
                    self.logger.error(f"No state abbreviations allowed.  Please update {state} to use the full state name.")
                    continue

                try:
                    # Assign the location name and location type
                    loc_name = name_type_split[0]
                    loc_type = location_types[name_type_split[1]]
                    self.logger.info(f"Processing {loc_name}-{loc_type}")
                except IndexError: # If the location name format is invalid
                    self.logger.error(f"Invalid location name format: {row['name']}.  Expected format is 'Location Name-Location Type'")
                    continue
                except KeyError as err: # If the location type is not BR or DC
                    self.logger.error(f"Invalid abbreviated location type, only BR or DC are allowed: {err}")
                    continue

                try:
                    location_type = LocationType.objects.get(name=loc_type)
                except LocationType.DoesNotExist:
                    self.logger.error(f"Location type '{location_type}' does not exist.  Please create the location type before importing data.")
                    continue


                try:
                    state_location, created = Location.objects.get_or_create(name=state, location_type=LocationType.objects.get(name="State"), status=active_status)
                    if created:
                        self.logger.info(f"Created state location: {state_location.name}")
                    else:
                        self.logger.info(f"State location already exists: {state_location.name}")
                except Exception as err:
                    self.logger.error(f"Error creating state location: {err}")
                    continue

                try:
                    city_location, created = Location.objects.get_or_create(name=city, location_type=LocationType.objects.get(name="City"), status=active_status)
                    if created:
                        self.logger.info(f"Created city location: {city_location.name}")
                    else:
                        self.logger.info(f"City location already exists: {city_location.name}")
                except Exception as err:
                    self.logger.error(f"Error creating city location: {err}")
                    continue
                    
                try:
                    loc_location, created = Location.objects.get_or_create(name=loc_name, location_type=location_type, status=active_status)
                    if created:
                        self.logger.info(f"Created location: {loc_location.name}")
                    else:
                        self.logger.info(f"Location already exists: {loc_location.name}")
                except Exception as err:
                    self.logger.error(f"Error creating location: {err}")
                    continue
        else:
            self.logger.error(f"Invalid import type: {import_type}")
            return

        self.logger.info("Imported Wayne Enterprises onboarding data from CSV file.")
