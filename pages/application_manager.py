from pages.element_panel import ElementPanel
from pages.simple_registration_page import SimpleRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.element_panel = ElementPanel()
        self.simple_registration_page = SimpleRegistrationPage()


app = ApplicationManager()
