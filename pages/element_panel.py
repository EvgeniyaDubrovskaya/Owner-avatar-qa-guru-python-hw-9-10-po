from selene import browser, have, command


class ElementPanel:
    def open(self):
        browser.open('/elements')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def open_simple_registration_form(self):
        browser.element('.left-pannel').all('[id^=item]').element_by(have.exact_text('Text Box')).click()
        return self
