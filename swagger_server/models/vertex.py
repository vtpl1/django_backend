# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Vertex(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, x: int=0, y: int=0):  # noqa: E501
        """Vertex - a model defined in Swagger

        :param x: The x of this Vertex.  # noqa: E501
        :type x: int
        :param y: The y of this Vertex.  # noqa: E501
        :type y: int
        """
        self.swagger_types = {
            'x': int,
            'y': int
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y'
        }
        self._x = x
        self._y = y

    @classmethod
    def from_dict(cls, dikt) -> 'Vertex':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vertex of this Vertex.  # noqa: E501
        :rtype: Vertex
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self) -> int:
        """Gets the x of this Vertex.


        :return: The x of this Vertex.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x: int):
        """Sets the x of this Vertex.


        :param x: The x of this Vertex.
        :type x: int
        """

        self._x = x

    @property
    def y(self) -> int:
        """Gets the y of this Vertex.


        :return: The y of this Vertex.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y: int):
        """Sets the y of this Vertex.


        :param y: The y of this Vertex.
        :type y: int
        """

        self._y = y