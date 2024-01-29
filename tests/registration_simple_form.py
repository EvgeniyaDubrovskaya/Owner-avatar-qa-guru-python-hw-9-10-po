from models.user import User
from pages.application_manager import ApplicationManager, app
from pages.simple_registration_page import SimpleRegistrationPage


def test_registrate_simple_user_success():
    user = User(first_name='Jane', last_name='Doe', email='jane@ru.ru')

    # app = ApplicationManager()
    app.element_panel.open()
    app.element_panel.open_simple_registration_form()

    app.simple_registration_page.register(user)
    app.simple_registration_page.should_have_registered_simple_user(user)


