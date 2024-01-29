from selene import browser, have, command
from helpers import resources
from models.user import User


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td:last-child')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_day_of_birth(self, year, month_name, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month_name)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def choose_sex(self, value):
        browser.all('[for^=gender-radio]').element_by(have.exact_text(value)).click()
        return self

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').click().type(value).press_enter()
        return self

    def select_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def add_picture(self, file_name):
        browser.element('.form-file-label').perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').send_keys(resources.path(file_name))
        return self

    def fill_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.element('#state').all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.element('#city').all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def submit_form(self):
        browser.element('#submit').press_enter()
        return self

    def should_have_registered_user_data(self, full_fio, email, sex, phone, date_of_birth, subject, hobby, file,
                                         address, state_city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_fio,
            email,
            sex,
            phone,
            date_of_birth,
            subject,
            hobby,
            file,
            address,
            state_city
        ))
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_sex(user.sex)
        self.fill_phone(user.phone)
        self.fill_day_of_birth(
            str(user.date_of_birth.year),
            str(user.date_of_birth.strftime("%B")),
            str(user.date_of_birth.day))
        self.fill_subject(user.subject)
        self.select_hobby(user.hobby)
        self.add_picture(user.picture)
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_form()
        return self

    def should_have_registered(self, user):
        self.should_have_registered_user_data(
            full_fio=f'{user.first_name} {user.last_name}',
            email=user.email,
            sex=user.sex,
            phone=user.phone,
            date_of_birth=f'{user.date_of_birth.strftime("%d %B")},{user.date_of_birth.year}',
            subject=user.subject,
            hobby=user.hobby,
            file=user.picture,
            address=user.address,
            state_city=f'{user.state} {user.city}'

        )
        return self
