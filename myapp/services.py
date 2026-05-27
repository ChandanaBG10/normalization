import pandas as pd

from .models import *
from .utils import *


def process_sap_file(file):

    df = pd.read_csv(file)

    company, _ = Company.objects.get_or_create(
        name="Demo Company"
    )

    source = DataSource.objects.create(
        company=company,
        source_type='sap',
        uploaded_file=file
    )

    for _, row in df.iterrows():

        quantity = float(row['quantity'])

        factor = 2.68

        emissions = calculate_emission(quantity, factor)

        suspicious = detect_suspicious(quantity)

        EmissionRecord.objects.create(
            company=company,
            data_source=source,

            category='Fuel',
            scope='Scope 1',

            activity_type=row['fuel_type'],

            quantity=quantity,

            unit=row['unit'],

            normalized_quantity=quantity,

            normalized_unit=row['unit'],

            emission_factor=factor,

            emissions=emissions,

            suspicious=suspicious
        )
def process_utility_file(file):

    df = pd.read_csv(file)

    company, _ = Company.objects.get_or_create(
        name="Demo Company"
    )

    source = DataSource.objects.create(
        company=company,
        source_type='utility',
        uploaded_file=file
    )

    for _, row in df.iterrows():

        quantity = float(row['kwh'])

        factor = 0.82

        emissions = calculate_emission(quantity, factor)

        suspicious = detect_suspicious(quantity)

        EmissionRecord.objects.create(
            company=company,
            data_source=source,

            category='Electricity',
            scope='Scope 2',

            activity_type='Electricity Usage',

            quantity=quantity,

            unit='kWh',

            normalized_quantity=quantity,

            normalized_unit='kWh',

            emission_factor=factor,

            emissions=emissions,

            suspicious=suspicious
        )

def process_travel_file(file):

    df = pd.read_csv(file)

    company, _ = Company.objects.get_or_create(
        name="Demo Company"
    )

    source = DataSource.objects.create(
        company=company,
        source_type='travel',
        uploaded_file=file
    )

    for _, row in df.iterrows():

        quantity = float(row['distance_km'])

        factor = 0.15

        emissions = calculate_emission(quantity, factor)

        suspicious = detect_suspicious(quantity)

        EmissionRecord.objects.create(
            company=company,
            data_source=source,

            category='Business Travel',

            scope='Scope 3',

            activity_type=row['travel_type'],

            quantity=quantity,

            unit='km',

            normalized_quantity=quantity,

            normalized_unit='km',

            emission_factor=factor,

            emissions=emissions,

            suspicious=suspicious
        )