#!/usr/bin/python3
"""Defines the City city."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city in AirBnB.

    Attributes:
        state_id (str): The state ID.
        name (str): The name of the CITY.
    """

    state_id = ""
    name = ""

