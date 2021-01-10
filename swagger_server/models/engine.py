# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.capability import Capability  # noqa: F401,E501
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server import util


class Engine(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, machine_id: str=None, capabilities: List[Capability]=None, updated: datetime=None, created: datetime=None, etag: str=None, links: Links=None):  # noqa: E501
        """Engine - a model defined in Swagger

        :param id: The id of this Engine.  # noqa: E501
        :type id: str
        :param machine_id: The machine_id of this Engine.  # noqa: E501
        :type machine_id: str
        :param capabilities: The capabilities of this Engine.  # noqa: E501
        :type capabilities: List[Capability]
        :param updated: The updated of this Engine.  # noqa: E501
        :type updated: datetime
        :param created: The created of this Engine.  # noqa: E501
        :type created: datetime
        :param etag: The etag of this Engine.  # noqa: E501
        :type etag: str
        :param links: The links of this Engine.  # noqa: E501
        :type links: Links
        """
        self.swagger_types = {
            'id': str,
            'machine_id': str,
            'capabilities': List[Capability],
            'updated': datetime,
            'created': datetime,
            'etag': str,
            'links': Links
        }

        self.attribute_map = {
            'id': '_id',
            'machine_id': 'machineId',
            'capabilities': 'capabilities',
            'updated': 'updated',
            'created': 'created',
            'etag': 'etag',
            'links': 'links'
        }
        self._id = id
        self._machine_id = machine_id
        self._capabilities = capabilities
        self._updated = updated
        self._created = created
        self._etag = etag
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'Engine':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The engine of this Engine.  # noqa: E501
        :rtype: Engine
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Engine.


        :return: The id of this Engine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Engine.


        :param id: The id of this Engine.
        :type id: str
        """

        self._id = id

    @property
    def machine_id(self) -> str:
        """Gets the machine_id of this Engine.


        :return: The machine_id of this Engine.
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id: str):
        """Sets the machine_id of this Engine.


        :param machine_id: The machine_id of this Engine.
        :type machine_id: str
        """

        self._machine_id = machine_id

    @property
    def capabilities(self) -> List[Capability]:
        """Gets the capabilities of this Engine.


        :return: The capabilities of this Engine.
        :rtype: List[Capability]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities: List[Capability]):
        """Sets the capabilities of this Engine.


        :param capabilities: The capabilities of this Engine.
        :type capabilities: List[Capability]
        """

        self._capabilities = capabilities

    @property
    def updated(self) -> datetime:
        """Gets the updated of this Engine.


        :return: The updated of this Engine.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated: datetime):
        """Sets the updated of this Engine.


        :param updated: The updated of this Engine.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def created(self) -> datetime:
        """Gets the created of this Engine.


        :return: The created of this Engine.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created: datetime):
        """Sets the created of this Engine.


        :param created: The created of this Engine.
        :type created: datetime
        """

        self._created = created

    @property
    def etag(self) -> str:
        """Gets the etag of this Engine.


        :return: The etag of this Engine.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag: str):
        """Sets the etag of this Engine.


        :param etag: The etag of this Engine.
        :type etag: str
        """

        self._etag = etag

    @property
    def links(self) -> Links:
        """Gets the links of this Engine.


        :return: The links of this Engine.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this Engine.


        :param links: The links of this Engine.
        :type links: Links
        """

        self._links = links