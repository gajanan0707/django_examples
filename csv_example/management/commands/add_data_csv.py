from django.core.management.base import BaseCommand
from csv_example.models import Employee


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_dump_data = [
            {"first_name": "Rachel", "last_name": "Booker", "location": "Manchester"},
            {"first_name": "Laura", "last_name": "Grey", "location": "London"},
            {"first_name": "Craig", "last_name": "Johnson", "location": "London"},
            {"first_name": "Mary", "last_name": "Jenkins", "location": "Manchester"},
            {"first_name": "Jamie", "last_name": "Smith", "location": "Manchester"},
        ]

        for data in csv_dump_data:
            unique = Employee.objects.filter(first_name=data["first_name"]).exists()
            print("unique", unique)
            if not unique:
                Employee.objects.create(**data)
