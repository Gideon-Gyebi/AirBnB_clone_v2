#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'  # Name of the database table
    name = Column(String(128), nullable=False)

    if getenv("HBNB TYPE STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """gettering for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    """ Define the relationship between State and City
    state = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        data = models.storage.all()
        city_data = []
        filtered_cities = []

        for data_key in data:
            city_name = data_key.replace('.', ' ')
            city_name_parts = shlex.split(city_name)

            if city_name_parts[0] == 'City':
                city_data.append(data[data_key])

        for city in city_data:
            if city.state_id == self.id:
                filtered_cities.append(city)

        return filtered_cities"""
