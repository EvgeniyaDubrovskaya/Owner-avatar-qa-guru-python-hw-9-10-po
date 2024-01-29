from datetime import date
from selene import have

from models.sex import Sex
from models.user import User
from pages.registration_page import RegistrationPage


def test_registrate_user_success():
    user = User(first_name='Jane', last_name='Doe', email='jane@doe.su', sex=Sex.Female, phone='1234567890',
                subject='Maths', hobby='Reading', picture='windy_hill.jpg',
                date_of_birth=date(1991, 1, 10),
                address='45 Current Address', state='NCR', city='Delhi')

    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.register(user)

    registration_page.should_have_registered(user)


