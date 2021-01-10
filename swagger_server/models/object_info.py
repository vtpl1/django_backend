# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object_direct_properties import ObjectDirectProperties  # noqa: F401,E501
from swagger_server.models.object_indirect_properties import ObjectIndirectProperties  # noqa: F401,E501
from swagger_server.models.object_rect import ObjectRect  # noqa: F401,E501
from swagger_server import util


class ObjectInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, object_direct_properties: ObjectDirectProperties=None, object_indirect_properties: ObjectIndirectProperties=None, object_type: str=None, object_rect: ObjectRect=None, confidence: float=0, is_valid: bool=False):  # noqa: E501
        """ObjectInfo - a model defined in Swagger

        :param object_direct_properties: The object_direct_properties of this ObjectInfo.  # noqa: E501
        :type object_direct_properties: ObjectDirectProperties
        :param object_indirect_properties: The object_indirect_properties of this ObjectInfo.  # noqa: E501
        :type object_indirect_properties: ObjectIndirectProperties
        :param object_type: The object_type of this ObjectInfo.  # noqa: E501
        :type object_type: str
        :param object_rect: The object_rect of this ObjectInfo.  # noqa: E501
        :type object_rect: ObjectRect
        :param confidence: The confidence of this ObjectInfo.  # noqa: E501
        :type confidence: float
        :param is_valid: The is_valid of this ObjectInfo.  # noqa: E501
        :type is_valid: bool
        """
        self.swagger_types = {
            'object_direct_properties': ObjectDirectProperties,
            'object_indirect_properties': ObjectIndirectProperties,
            'object_type': str,
            'object_rect': ObjectRect,
            'confidence': float,
            'is_valid': bool
        }

        self.attribute_map = {
            'object_direct_properties': 'objectDirectProperties',
            'object_indirect_properties': 'objectIndirectProperties',
            'object_type': 'objectType',
            'object_rect': 'objectRect',
            'confidence': 'confidence',
            'is_valid': 'isValid'
        }
        self._object_direct_properties = object_direct_properties
        self._object_indirect_properties = object_indirect_properties
        self._object_type = object_type
        self._object_rect = object_rect
        self._confidence = confidence
        self._is_valid = is_valid

    @classmethod
    def from_dict(cls, dikt) -> 'ObjectInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The objectInfo of this ObjectInfo.  # noqa: E501
        :rtype: ObjectInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_direct_properties(self) -> ObjectDirectProperties:
        """Gets the object_direct_properties of this ObjectInfo.


        :return: The object_direct_properties of this ObjectInfo.
        :rtype: ObjectDirectProperties
        """
        return self._object_direct_properties

    @object_direct_properties.setter
    def object_direct_properties(self, object_direct_properties: ObjectDirectProperties):
        """Sets the object_direct_properties of this ObjectInfo.


        :param object_direct_properties: The object_direct_properties of this ObjectInfo.
        :type object_direct_properties: ObjectDirectProperties
        """

        self._object_direct_properties = object_direct_properties

    @property
    def object_indirect_properties(self) -> ObjectIndirectProperties:
        """Gets the object_indirect_properties of this ObjectInfo.


        :return: The object_indirect_properties of this ObjectInfo.
        :rtype: ObjectIndirectProperties
        """
        return self._object_indirect_properties

    @object_indirect_properties.setter
    def object_indirect_properties(self, object_indirect_properties: ObjectIndirectProperties):
        """Sets the object_indirect_properties of this ObjectInfo.


        :param object_indirect_properties: The object_indirect_properties of this ObjectInfo.
        :type object_indirect_properties: ObjectIndirectProperties
        """

        self._object_indirect_properties = object_indirect_properties

    @property
    def object_type(self) -> str:
        """Gets the object_type of this ObjectInfo.


        :return: The object_type of this ObjectInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: str):
        """Sets the object_type of this ObjectInfo.


        :param object_type: The object_type of this ObjectInfo.
        :type object_type: str
        """

        self._object_type = object_type

    @property
    def object_rect(self) -> ObjectRect:
        """Gets the object_rect of this ObjectInfo.


        :return: The object_rect of this ObjectInfo.
        :rtype: ObjectRect
        """
        return self._object_rect

    @object_rect.setter
    def object_rect(self, object_rect: ObjectRect):
        """Sets the object_rect of this ObjectInfo.


        :param object_rect: The object_rect of this ObjectInfo.
        :type object_rect: ObjectRect
        """

        self._object_rect = object_rect

    @property
    def confidence(self) -> float:
        """Gets the confidence of this ObjectInfo.


        :return: The confidence of this ObjectInfo.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: float):
        """Sets the confidence of this ObjectInfo.


        :param confidence: The confidence of this ObjectInfo.
        :type confidence: float
        """

        self._confidence = confidence

    @property
    def is_valid(self) -> bool:
        """Gets the is_valid of this ObjectInfo.


        :return: The is_valid of this ObjectInfo.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid: bool):
        """Sets the is_valid of this ObjectInfo.


        :param is_valid: The is_valid of this ObjectInfo.
        :type is_valid: bool
        """

        self._is_valid = is_valid