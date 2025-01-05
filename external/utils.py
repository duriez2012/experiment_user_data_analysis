import random


def generate_user_id():
    return f"u{random.randint(1, 1000000):06d}"

