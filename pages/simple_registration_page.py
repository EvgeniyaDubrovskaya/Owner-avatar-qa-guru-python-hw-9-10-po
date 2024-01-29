from selene import browser, have, command

from models.user import User


class SimpleRegistrationPage:
    def open(self):
        browser.open('/text-box')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_name(self, value):
        browser.element('#userName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def register(self, user: User):
        self.fill_name(user.first_last_name())
        self.fill_email(user.email)
        self.submit()

    def should_have_registered_simple_user(self, user: User):
        browser.element('#output').element('#name').should(have.text(user.first_last_name()))
        browser.element('#output').element('#email').should(have.text(user.email))
        return self
