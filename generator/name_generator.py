from faker import Faker
import random
from datetime import datetime, timedelta
import csv


class NameGenerator:

    def generate_random_data(self):
        fake = Faker()
        firstname = fake.first_name()
        surname = fake.last_name()
        othernames = fake.first_name()
        gender = random.choice(['Male', 'Female'])
        phone = fake.phone_number()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
        date_of_employment = fake.date_between(date_of_birth, end_date='today')
        email = fake.email()
        tpin = ''.join(fake.random_elements(elements='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', length=13))
        idno = fake.random_number(digits=8)
        staffno = ''.join(fake.random_elements(elements='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', length=6))

        return {
            'firstname': firstname,
            'surname': surname,
            'othernames': othernames,
            'gender': gender,
            'phone': phone,
            'date_of_birth': date_of_birth,
            'date_of_employment': date_of_employment,
            'email': email,
            'tpin': tpin,
            'idno': idno,
            'staffno': staffno
        }

    def generate_names(self, count: int):
        records = [self.generate_random_data() for _ in range(count)]
        self.export_csv(records)
        return {'message': 'Done'}

    def export_csv(self, records):
        with open('generated_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['firstname', 'surname', 'othernames', 'gender', 'phone', 'date_of_birth', 'date_of_employment', 'email', 'tpin', 'idno', 'staffno']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for record in records:
                writer.writerow(record)
