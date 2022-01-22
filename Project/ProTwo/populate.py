import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

from faker import Faker
from AppTwo.models import User

fake = Faker()

def populate(N=5):

    for entry in range(N):
        fake_fname = fake.first_name()
        fake_lname = fake.last_name()
        fake_email = fake.email()

        # Now Creating new entry (object)
        fake_user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating Users File")
    populate(20)
    print("Complete!")