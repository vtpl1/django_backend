# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Extra(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, key: str=None, value: str=None):  # noqa: E501
        """Extra - a model defined in Swagger

        :param key: The key of this Extra.  # noqa: E501
        :type key: str
        :param value: The value of this Extra.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'key': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }
        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Extra':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The extra of this Extra.  # noqa: E501
        :rtype: Extra
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self) -> str:
        """Gets the key of this Extra.


        :return: The key of this Extra.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this Extra.


        :param key: The key of this Extra.
        :type key: str
        """

        self._key = key

    @property
    def value(self) -> str:
        """Gets the value of this Extra.


        :return: The value of this Extra.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Extra.


        :param value: The value of this Extra.
        :type value: str
        """

        self._value = value
