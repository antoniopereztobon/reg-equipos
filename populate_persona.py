import os

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azureproject.settings")

settings_module = 'azureproject.production' if 'WEBSITE_HOSTNAME' in os.environ else 'azureproject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

import django

django.setup()

import csv
from django.core.management.base import BaseCommand
from ingreso.models import Persona


def populate(N):
    with open("persona.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Columnas: {", ".join(row)}')
                line_count += 1
            else:
                id_tipo = "CC"
                id_num = row[0]
                nom_persona = row[1]
                try:
                    persona = Persona.objects.create(id_tipo=id_tipo, id_num=id_num, nom_persona=nom_persona)
                except Exception as e:
                    print(f'Error: {str(e)}; línea: {line_count}; nombre: {nom_persona}')

                line_count += 1

            if line_count > N:
                break

        print(f"Processed {line_count} lines.")


if __name__ == "__main__":
    print("populating script!")
    populate(5000)
    print("populating complete!")
