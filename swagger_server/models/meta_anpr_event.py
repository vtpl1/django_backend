# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.color import Color  # noqa: F401,E501
from swagger_server.models.vehicle_type import VehicleType  # noqa: F401,E501
from swagger_server import util


class MetaAnprEvent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, vehicle_number: str=None, vehicle_type: VehicleType=None, vehicle_color: Color=None, vehicle_make: str=None, vehicle_model: str=None, count_of_vehicle: int=0, count_of_two_wheeler: int=0, count_of_helmet: int=0, count_of_no_helmet: int=0, count_of_triple_ride: int=0):  # noqa: E501
        """MetaAnprEvent - a model defined in Swagger

        :param vehicle_number: The vehicle_number of this MetaAnprEvent.  # noqa: E501
        :type vehicle_number: str
        :param vehicle_type: The vehicle_type of this MetaAnprEvent.  # noqa: E501
        :type vehicle_type: VehicleType
        :param vehicle_color: The vehicle_color of this MetaAnprEvent.  # noqa: E501
        :type vehicle_color: Color
        :param vehicle_make: The vehicle_make of this MetaAnprEvent.  # noqa: E501
        :type vehicle_make: str
        :param vehicle_model: The vehicle_model of this MetaAnprEvent.  # noqa: E501
        :type vehicle_model: str
        :param count_of_vehicle: The count_of_vehicle of this MetaAnprEvent.  # noqa: E501
        :type count_of_vehicle: int
        :param count_of_two_wheeler: The count_of_two_wheeler of this MetaAnprEvent.  # noqa: E501
        :type count_of_two_wheeler: int
        :param count_of_helmet: The count_of_helmet of this MetaAnprEvent.  # noqa: E501
        :type count_of_helmet: int
        :param count_of_no_helmet: The count_of_no_helmet of this MetaAnprEvent.  # noqa: E501
        :type count_of_no_helmet: int
        :param count_of_triple_ride: The count_of_triple_ride of this MetaAnprEvent.  # noqa: E501
        :type count_of_triple_ride: int
        """
        self.swagger_types = {
            'vehicle_number': str,
            'vehicle_type': VehicleType,
            'vehicle_color': Color,
            'vehicle_make': str,
            'vehicle_model': str,
            'count_of_vehicle': int,
            'count_of_two_wheeler': int,
            'count_of_helmet': int,
            'count_of_no_helmet': int,
            'count_of_triple_ride': int
        }

        self.attribute_map = {
            'vehicle_number': 'vehicleNumber',
            'vehicle_type': 'vehicleType',
            'vehicle_color': 'vehicleColor',
            'vehicle_make': 'vehicleMake',
            'vehicle_model': 'vehicleModel',
            'count_of_vehicle': 'countOfVehicle',
            'count_of_two_wheeler': 'countOfTwoWheeler',
            'count_of_helmet': 'countOfHelmet',
            'count_of_no_helmet': 'countOfNoHelmet',
            'count_of_triple_ride': 'countOfTripleRide'
        }
        self._vehicle_number = vehicle_number
        self._vehicle_type = vehicle_type
        self._vehicle_color = vehicle_color
        self._vehicle_make = vehicle_make
        self._vehicle_model = vehicle_model
        self._count_of_vehicle = count_of_vehicle
        self._count_of_two_wheeler = count_of_two_wheeler
        self._count_of_helmet = count_of_helmet
        self._count_of_no_helmet = count_of_no_helmet
        self._count_of_triple_ride = count_of_triple_ride

    @classmethod
    def from_dict(cls, dikt) -> 'MetaAnprEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metaAnprEvent of this MetaAnprEvent.  # noqa: E501
        :rtype: MetaAnprEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vehicle_number(self) -> str:
        """Gets the vehicle_number of this MetaAnprEvent.

        Vehicle number detected in OCR  # noqa: E501

        :return: The vehicle_number of this MetaAnprEvent.
        :rtype: str
        """
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, vehicle_number: str):
        """Sets the vehicle_number of this MetaAnprEvent.

        Vehicle number detected in OCR  # noqa: E501

        :param vehicle_number: The vehicle_number of this MetaAnprEvent.
        :type vehicle_number: str
        """

        self._vehicle_number = vehicle_number

    @property
    def vehicle_type(self) -> VehicleType:
        """Gets the vehicle_type of this MetaAnprEvent.


        :return: The vehicle_type of this MetaAnprEvent.
        :rtype: VehicleType
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type: VehicleType):
        """Sets the vehicle_type of this MetaAnprEvent.


        :param vehicle_type: The vehicle_type of this MetaAnprEvent.
        :type vehicle_type: VehicleType
        """

        self._vehicle_type = vehicle_type

    @property
    def vehicle_color(self) -> Color:
        """Gets the vehicle_color of this MetaAnprEvent.


        :return: The vehicle_color of this MetaAnprEvent.
        :rtype: Color
        """
        return self._vehicle_color

    @vehicle_color.setter
    def vehicle_color(self, vehicle_color: Color):
        """Sets the vehicle_color of this MetaAnprEvent.


        :param vehicle_color: The vehicle_color of this MetaAnprEvent.
        :type vehicle_color: Color
        """

        self._vehicle_color = vehicle_color

    @property
    def vehicle_make(self) -> str:
        """Gets the vehicle_make of this MetaAnprEvent.


        :return: The vehicle_make of this MetaAnprEvent.
        :rtype: str
        """
        return self._vehicle_make

    @vehicle_make.setter
    def vehicle_make(self, vehicle_make: str):
        """Sets the vehicle_make of this MetaAnprEvent.


        :param vehicle_make: The vehicle_make of this MetaAnprEvent.
        :type vehicle_make: str
        """

        self._vehicle_make = vehicle_make

    @property
    def vehicle_model(self) -> str:
        """Gets the vehicle_model of this MetaAnprEvent.


        :return: The vehicle_model of this MetaAnprEvent.
        :rtype: str
        """
        return self._vehicle_model

    @vehicle_model.setter
    def vehicle_model(self, vehicle_model: str):
        """Sets the vehicle_model of this MetaAnprEvent.


        :param vehicle_model: The vehicle_model of this MetaAnprEvent.
        :type vehicle_model: str
        """

        self._vehicle_model = vehicle_model

    @property
    def count_of_vehicle(self) -> int:
        """Gets the count_of_vehicle of this MetaAnprEvent.


        :return: The count_of_vehicle of this MetaAnprEvent.
        :rtype: int
        """
        return self._count_of_vehicle

    @count_of_vehicle.setter
    def count_of_vehicle(self, count_of_vehicle: int):
        """Sets the count_of_vehicle of this MetaAnprEvent.


        :param count_of_vehicle: The count_of_vehicle of this MetaAnprEvent.
        :type count_of_vehicle: int
        """

        self._count_of_vehicle = count_of_vehicle

    @property
    def count_of_two_wheeler(self) -> int:
        """Gets the count_of_two_wheeler of this MetaAnprEvent.


        :return: The count_of_two_wheeler of this MetaAnprEvent.
        :rtype: int
        """
        return self._count_of_two_wheeler

    @count_of_two_wheeler.setter
    def count_of_two_wheeler(self, count_of_two_wheeler: int):
        """Sets the count_of_two_wheeler of this MetaAnprEvent.


        :param count_of_two_wheeler: The count_of_two_wheeler of this MetaAnprEvent.
        :type count_of_two_wheeler: int
        """

        self._count_of_two_wheeler = count_of_two_wheeler

    @property
    def count_of_helmet(self) -> int:
        """Gets the count_of_helmet of this MetaAnprEvent.


        :return: The count_of_helmet of this MetaAnprEvent.
        :rtype: int
        """
        return self._count_of_helmet

    @count_of_helmet.setter
    def count_of_helmet(self, count_of_helmet: int):
        """Sets the count_of_helmet of this MetaAnprEvent.


        :param count_of_helmet: The count_of_helmet of this MetaAnprEvent.
        :type count_of_helmet: int
        """

        self._count_of_helmet = count_of_helmet

    @property
    def count_of_no_helmet(self) -> int:
        """Gets the count_of_no_helmet of this MetaAnprEvent.


        :return: The count_of_no_helmet of this MetaAnprEvent.
        :rtype: int
        """
        return self._count_of_no_helmet

    @count_of_no_helmet.setter
    def count_of_no_helmet(self, count_of_no_helmet: int):
        """Sets the count_of_no_helmet of this MetaAnprEvent.


        :param count_of_no_helmet: The count_of_no_helmet of this MetaAnprEvent.
        :type count_of_no_helmet: int
        """

        self._count_of_no_helmet = count_of_no_helmet

    @property
    def count_of_triple_ride(self) -> int:
        """Gets the count_of_triple_ride of this MetaAnprEvent.


        :return: The count_of_triple_ride of this MetaAnprEvent.
        :rtype: int
        """
        return self._count_of_triple_ride

    @count_of_triple_ride.setter
    def count_of_triple_ride(self, count_of_triple_ride: int):
        """Sets the count_of_triple_ride of this MetaAnprEvent.


        :param count_of_triple_ride: The count_of_triple_ride of this MetaAnprEvent.
        :type count_of_triple_ride: int
        """

        self._count_of_triple_ride = count_of_triple_ride
