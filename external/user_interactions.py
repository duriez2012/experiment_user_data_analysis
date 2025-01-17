import csv
import random
from datetime import datetime, timedelta

from external.utils import generate_user_id


def generate_user_interactions(num_records, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user_id', 'timestamp', 'action_type', 'page_id', 'duration_ms', 'app_version'])
        for _ in range(num_records):
            writer.writerow([
                generate_user_id(),
                generate_timestamp().strftime("%Y-%m-%d %H:%M:%S"),
                generate_action_type(),
                generate_page_id(),
                generate_duration_ms(),
                generate_app_version()
            ])


def generate_timestamp():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))


def generate_action_type():
    return random.choice(['page_view', 'edit', 'create', 'delete', 'share'])


def generate_page_id():
    return f"p{random.randint(1, 1000000):06d}"


def generate_duration_ms():
    return random.randint(100, 300000)


def generate_app_version():
    major = random.randint(5, 7)
    minor = random.randint(0, 9)
    patch = random.randint(0, 9)
    return f"{major}.{minor}.{patch}"