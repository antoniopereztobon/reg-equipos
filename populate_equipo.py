import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azureproject.settings")

import django

django.setup()

import csv
from django.core.management.base import BaseCommand
from ingreso.models import Equipo


def populate(N):
    with open("equipo.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Columnas: {", ".join(row)}')
                line_count += 1
            else:
                eq_tipo = row[0]
                eq_marca = row[1]
                eq_serie = row[2]
                equipo = Equipo.objects.create(eq_tipo=eq_tipo, eq_marca=eq_marca, eq_serie=eq_serie)

                line_count += 1

            if line_count > N:
                break

        print(f"Processed {line_count} lines.")


if __name__ == "__main__":
    print("populating script!")
    populate(5000)
    print("populating complete!")
