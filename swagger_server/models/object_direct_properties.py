# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object_dimension import ObjectDimension  # noqa: F401,E501
from swagger_server import util


class ObjectDirectProperties(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, color: str=None, speed: float=0, object_dimension: ObjectDimension=None):  # noqa: E501
        """ObjectDirectProperties - a model defined in Swagger

        :param color: The color of this ObjectDirectProperties.  # noqa: E501
        :type color: str
        :param speed: The speed of this ObjectDirectProperties.  # noqa: E501
        :type speed: float
        :param object_dimension: The object_dimension of this ObjectDirectProperties.  # noqa: E501
        :type object_dimension: ObjectDimension
        """
        self.swagger_types = {
            'color': str,
            'speed': float,
            'object_dimension': ObjectDimension
        }

        self.attribute_map = {
            'color': 'color',
            'speed': 'speed',
            'object_dimension': 'objectDimension'
        }
        self._color = color
        self._speed = speed
        self._object_dimension = object_dimension

    @classmethod
    def from_dict(cls, dikt) -> 'ObjectDirectProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The objectDirectProperties of this ObjectDirectProperties.  # noqa: E501
        :rtype: ObjectDirectProperties
        """
        return util.deserialize_model(dikt, cls)

    @property
    def color(self) -> str:
        """Gets the color of this ObjectDirectProperties.


        :return: The color of this ObjectDirectProperties.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color: str):
        """Sets the color of this ObjectDirectProperties.


        :param color: The color of this ObjectDirectProperties.
        :type color: str
        """

        self._color = color

    @property
    def speed(self) -> float:
        """Gets the speed of this ObjectDirectProperties.


        :return: The speed of this ObjectDirectProperties.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed: float):
        """Sets the speed of this ObjectDirectProperties.


        :param speed: The speed of this ObjectDirectProperties.
        :type speed: float
        """

        self._speed = speed

    @property
    def object_dimension(self) -> ObjectDimension:
        """Gets the object_dimension of this ObjectDirectProperties.


        :return: The object_dimension of this ObjectDirectProperties.
        :rtype: ObjectDimension
        """
        return self._object_dimension

    @object_dimension.setter
    def object_dimension(self, object_dimension: ObjectDimension):
        """Sets the object_dimension of this ObjectDirectProperties.


        :param object_dimension: The object_dimension of this ObjectDirectProperties.
        :type object_dimension: ObjectDimension
        """

        self._object_dimension = object_dimension
