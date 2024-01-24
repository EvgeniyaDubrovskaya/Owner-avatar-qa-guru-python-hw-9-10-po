from selene import browser, have, command
from helpers import resources


class RegistrationPage:

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

    def fill_day_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month)).click()
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
