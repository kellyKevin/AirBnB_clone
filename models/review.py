#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review in AirBnB.

    Attributes:
        place_id (str): The Place ID.
        user_id (str): The User ID.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

