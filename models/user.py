from dataclasses import dataclass
from datetime import date

from models.sex import Sex
from typing import Optional


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    sex: Optional[Sex] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    subject: Optional[str] = None
    hobby: Optional[str] = None
    picture: Optional[str] = None
    address: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None

    def first_last_name(self):
        return f'{self.first_name} {self.last_name}'




