#!/usr/bin/python3
"""This is the amenity class"""
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity which Inherits
        from SQLAlchemy Base and links to the MySQL table amenities
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
