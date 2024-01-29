from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    sex: str
    phone: str
    date_of_birth: date
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str




