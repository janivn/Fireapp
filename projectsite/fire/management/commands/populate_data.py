import random
from django.core.management.base import BaseCommand
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions
from django.utils import timezone
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create Locations
        location1 = Locations.objects.create(
            name='Baker"s Hill',
            latitude=Decimal('9.807576'),
            longitude=Decimal('118.732099'),
            address='Santa Monica',
            city='Puerto Princesa',
            country='Philippines'
        )




        location2 = Locations.objects.create(
            name='Barangay San Jose',
            latitude=Decimal('9.803232'),
            longitude=Decimal(' 118.755201'),
            address='Barangay San Jose, Puerto Princesa, 5300 Palawan',
            city='Puerto Princesa',
            country='Philippines'
        )

        # Create FireStations
        station1 = FireStation.objects.create(
            name='Puerto Princesa Central Fire Station',
            latitude=Decimal('9.7404'),
            longitude=Decimal('118.7330'),
            address='Malvar St, Barangay Tagumpay',
            city='Puerto Princesa',
            country='Philippines'
        )
        station2 = FireStation.objects.create(
            name='Puerto Princesa North Fire Station',
            latitude=Decimal('9.7722'),
            longitude=Decimal('118.7516'),
            address='Hagedorn Rd, Barangay San Miguel',
            city='Puerto Princesa',
            country='Philippines'
        )

        # Create Incidents
        for _ in range(10):
            random_location = random.choice([location1, location2])
            random_severity = random.choice(['Minor Fire', 'Moderate Fire', 'Major Fire'])
            Incident.objects.create(
                location=random_location,
                date_time=timezone.now(),
                severity_level=random_severity,
                description='A fire incident occurred.'
            )

        # Create Firefighters (Example data for simplicity)
        firefighter1 = Firefighters.objects.create(
            name='John Doe',
            rank='Captain',
            experience_level='Firefighter III',
            station='Puerto Princesa Central Fire Station'
        )
        firefighter2 = Firefighters.objects.create(
            name='Jane Smith',
            rank='Battalion Chief',
            experience_level='Firefighter II',
            station='Puerto Princesa North Fire Station'
        )

        # Create FireTrucks (Example data for simplicity)
        firetruck1 = FireTruck.objects.create(
            truck_number='Truck 101',
            model='Model A',
            capacity='1000L',
            station=station1
        )
        firetruck2 = FireTruck.objects.create(
            truck_number='Truck 202',
            model='Model B',
            capacity='1500L',
            station=station2
        )

        # Create WeatherConditions (Example data for simplicity)
        for incident in Incident.objects.all():
            WeatherConditions.objects.create(
                incident=incident,
                temperature=Decimal(random.uniform(25, 35)),
                humidity=Decimal(random.uniform(40, 60)),
                wind_speed=Decimal(random.uniform(5, 15)),
                weather_description='Variable weather conditions.'
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))
