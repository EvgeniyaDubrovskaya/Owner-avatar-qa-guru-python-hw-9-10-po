from pages.registration_page import RegistrationPage


def test_registrate_user_success():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Jane')
    registration_page.fill_last_name('Doe')
    registration_page.fill_email('jane@doe.su')
    registration_page.choose_sex('Female')
    registration_page.fill_phone('1234567890')
    registration_page.fill_day_of_birth('1991', 'January', '10')
    registration_page.fill_subject('Maths')
    registration_page.select_hobby('Reading')
    registration_page.add_picture('windy_hill.jpg')
    registration_page.fill_address('45 Current Address')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')

    registration_page.submit_form()

    registration_page.should_have_registered_user_data(
        'Jane Doe',
        'jane@doe.su',
        'Female',
        '1234567890',
        '10 January,1991',
        'Maths',
        'Reading',
        'windy_hill.jpg',
        '45 Current Address',
        'NCR Delhi'
    )
