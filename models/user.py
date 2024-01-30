from dataclasses import dataclass
from datetime import date

from models.sex import Sex


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    sex: Sex
    phone: str
    date_of_birth: date
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str

    def first_last_name(self):
        return f'{self.first_name} {self.last_name}'
