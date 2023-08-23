#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv, environ
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship


# Define place_amenity table for Many-To-Many relationship
place_amenity = Table('place_amenity', Base.metadata,
                Column('place_id', String(60), ForeignKey('places.id'),
                    primary_key=True, nullable=False),
                Column('amenity_id', String(60), ForeignKey('amenities.id'),
                    primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places';
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')

    else:
        @property
        def reviews(self) -> list:
            """reviews list"""
            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        if environ.get('HBNB_TYPE_STORAGE') == 'db':
            amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="place_amenities")
        
        else:
        @property
        def amenities(self) -> list:
            """amenities list"""
            amenities_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id == self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj: Amenity):
            if type(obj) != Amenity or obj is None:
                return
            else:
                self.amenity_ids.append(obj.id)
