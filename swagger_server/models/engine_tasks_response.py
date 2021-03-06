# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.engine_task import EngineTask  # noqa: F401,E501
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server.models.meta import Meta  # noqa: F401,E501
from swagger_server import util


class EngineTasksResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, items: List[EngineTask]=None, links: Links=None, meta: Meta=None):  # noqa: E501
        """EngineTasksResponse - a model defined in Swagger

        :param items: The items of this EngineTasksResponse.  # noqa: E501
        :type items: List[EngineTask]
        :param links: The links of this EngineTasksResponse.  # noqa: E501
        :type links: Links
        :param meta: The meta of this EngineTasksResponse.  # noqa: E501
        :type meta: Meta
        """
        self.swagger_types = {
            'items': List[EngineTask],
            'links': Links,
            'meta': Meta
        }

        self.attribute_map = {
            'items': 'items',
            'links': 'links',
            'meta': 'meta'
        }
        self._items = items
        self._links = links
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'EngineTasksResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The engineTasksResponse of this EngineTasksResponse.  # noqa: E501
        :rtype: EngineTasksResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self) -> List[EngineTask]:
        """Gets the items of this EngineTasksResponse.


        :return: The items of this EngineTasksResponse.
        :rtype: List[EngineTask]
        """
        return self._items

    @items.setter
    def items(self, items: List[EngineTask]):
        """Sets the items of this EngineTasksResponse.


        :param items: The items of this EngineTasksResponse.
        :type items: List[EngineTask]
        """

        self._items = items

    @property
    def links(self) -> Links:
        """Gets the links of this EngineTasksResponse.


        :return: The links of this EngineTasksResponse.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this EngineTasksResponse.


        :param links: The links of this EngineTasksResponse.
        :type links: Links
        """

        self._links = links

    @property
    def meta(self) -> Meta:
        """Gets the meta of this EngineTasksResponse.


        :return: The meta of this EngineTasksResponse.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: Meta):
        """Sets the meta of this EngineTasksResponse.


        :param meta: The meta of this EngineTasksResponse.
        :type meta: Meta
        """

        self._meta = meta
