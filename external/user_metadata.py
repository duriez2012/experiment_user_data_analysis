import csv
import random
from datetime import datetime, timedelta

from external.utils import generate_user_id


def generate_user_metadata(num_records, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile
                            )
        writer.writerow(['user_id', 'join_date', 'country', 'device_type', 'subscription_type'])
        for _ in range(num_records):
            writer.writerow([
                generate_user_id(),
                generate_join_date().strftime("%Y-%m-%d"),
                generate_country(),
                generate_device_type(),
                generate_subscription_type()
            ])


def generate_join_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


def generate_country():
    return random.choice(['US', 'UK', 'CA', 'AU', 'DE', 'FR', 'JP', 'IN', 'BR', 'MX'])


def generate_device_type():
    return random.choice(['iPhone', 'iPad', 'Android Phone', 'Android Tablet', 'Windows', 'Mac'])


def generate_subscription_type():
    return random.choice(['free', 'basic', 'premium', 'enterprise'])