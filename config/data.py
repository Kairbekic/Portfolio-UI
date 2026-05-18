import os
from dotenv import load_dotenv
from faker import Faker

load_dotenv()
fake = Faker()

class Data:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    FIRST_NAME = fake.first_name()
    LAST_NAME = fake.last_name()
    EMPLOYEE_ID = fake.random_int(999, 9999)
