# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.capability import Capability  # noqa: F401,E501
from swagger_server.models.event import Event  # noqa: F401,E501
from swagger_server.models.event_details import EventDetails  # noqa: F401,E501
from swagger_server.models.event_type import EventType  # noqa: F401,E501
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server.models.meta_attribute_event import MetaAttributeEvent  # noqa: F401,E501
from swagger_server import util


class AttributeEvent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, capbilities_type: Capability=None, event_type: EventType=None, event_details: EventDetails=None, event_snaps: List[str]=None, event_clips: List[str]=None, updated: datetime=None, created: datetime=None, etag: str=None, links: Links=None, meta_attribute_event: MetaAttributeEvent=None):  # noqa: E501
        """AttributeEvent - a model defined in Swagger

        :param id: The id of this AttributeEvent.  # noqa: E501
        :type id: str
        :param capbilities_type: The capbilities_type of this AttributeEvent.  # noqa: E501
        :type capbilities_type: Capability
        :param event_type: The event_type of this AttributeEvent.  # noqa: E501
        :type event_type: EventType
        :param event_details: The event_details of this AttributeEvent.  # noqa: E501
        :type event_details: EventDetails
        :param event_snaps: The event_snaps of this AttributeEvent.  # noqa: E501
        :type event_snaps: List[str]
        :param event_clips: The event_clips of this AttributeEvent.  # noqa: E501
        :type event_clips: List[str]
        :param updated: The updated of this AttributeEvent.  # noqa: E501
        :type updated: datetime
        :param created: The created of this AttributeEvent.  # noqa: E501
        :type created: datetime
        :param etag: The etag of this AttributeEvent.  # noqa: E501
        :type etag: str
        :param links: The links of this AttributeEvent.  # noqa: E501
        :type links: Links
        :param meta_attribute_event: The meta_attribute_event of this AttributeEvent.  # noqa: E501
        :type meta_attribute_event: MetaAttributeEvent
        """
        self.swagger_types = {
            'id': str,
            'capbilities_type': Capability,
            'event_type': EventType,
            'event_details': EventDetails,
            'event_snaps': List[str],
            'event_clips': List[str],
            'updated': datetime,
            'created': datetime,
            'etag': str,
            'links': Links,
            'meta_attribute_event': MetaAttributeEvent
        }

        self.attribute_map = {
            'id': '_id',
            'capbilities_type': 'capbilitiesType',
            'event_type': 'eventType',
            'event_details': 'eventDetails',
            'event_snaps': 'eventSnaps',
            'event_clips': 'eventClips',
            'updated': 'updated',
            'created': 'created',
            'etag': 'etag',
            'links': 'links',
            'meta_attribute_event': 'metaAttributeEvent'
        }
        self._id = id
        self._capbilities_type = capbilities_type
        self._event_type = event_type
        self._event_details = event_details
        self._event_snaps = event_snaps
        self._event_clips = event_clips
        self._updated = updated
        self._created = created
        self._etag = etag
        self._links = links
        self._meta_attribute_event = meta_attribute_event

    @classmethod
    def from_dict(cls, dikt) -> 'AttributeEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The attributeEvent of this AttributeEvent.  # noqa: E501
        :rtype: AttributeEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this AttributeEvent.


        :return: The id of this AttributeEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AttributeEvent.


        :param id: The id of this AttributeEvent.
        :type id: str
        """

        self._id = id

    @property
    def capbilities_type(self) -> Capability:
        """Gets the capbilities_type of this AttributeEvent.


        :return: The capbilities_type of this AttributeEvent.
        :rtype: Capability
        """
        return self._capbilities_type

    @capbilities_type.setter
    def capbilities_type(self, capbilities_type: Capability):
        """Sets the capbilities_type of this AttributeEvent.


        :param capbilities_type: The capbilities_type of this AttributeEvent.
        :type capbilities_type: Capability
        """

        self._capbilities_type = capbilities_type

    @property
    def event_type(self) -> EventType:
        """Gets the event_type of this AttributeEvent.


        :return: The event_type of this AttributeEvent.
        :rtype: EventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: EventType):
        """Sets the event_type of this AttributeEvent.


        :param event_type: The event_type of this AttributeEvent.
        :type event_type: EventType
        """

        self._event_type = event_type

    @property
    def event_details(self) -> EventDetails:
        """Gets the event_details of this AttributeEvent.


        :return: The event_details of this AttributeEvent.
        :rtype: EventDetails
        """
        return self._event_details

    @event_details.setter
    def event_details(self, event_details: EventDetails):
        """Sets the event_details of this AttributeEvent.


        :param event_details: The event_details of this AttributeEvent.
        :type event_details: EventDetails
        """

        self._event_details = event_details

    @property
    def event_snaps(self) -> List[str]:
        """Gets the event_snaps of this AttributeEvent.

        _id of snap from #$ref: '#/components/schemas/snap'  # noqa: E501

        :return: The event_snaps of this AttributeEvent.
        :rtype: List[str]
        """
        return self._event_snaps

    @event_snaps.setter
    def event_snaps(self, event_snaps: List[str]):
        """Sets the event_snaps of this AttributeEvent.

        _id of snap from #$ref: '#/components/schemas/snap'  # noqa: E501

        :param event_snaps: The event_snaps of this AttributeEvent.
        :type event_snaps: List[str]
        """

        self._event_snaps = event_snaps

    @property
    def event_clips(self) -> List[str]:
        """Gets the event_clips of this AttributeEvent.

        _id of snap from #$ref: '#/components/schemas/clip'  # noqa: E501

        :return: The event_clips of this AttributeEvent.
        :rtype: List[str]
        """
        return self._event_clips

    @event_clips.setter
    def event_clips(self, event_clips: List[str]):
        """Sets the event_clips of this AttributeEvent.

        _id of snap from #$ref: '#/components/schemas/clip'  # noqa: E501

        :param event_clips: The event_clips of this AttributeEvent.
        :type event_clips: List[str]
        """

        self._event_clips = event_clips

    @property
    def updated(self) -> datetime:
        """Gets the updated of this AttributeEvent.


        :return: The updated of this AttributeEvent.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated: datetime):
        """Sets the updated of this AttributeEvent.


        :param updated: The updated of this AttributeEvent.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def created(self) -> datetime:
        """Gets the created of this AttributeEvent.


        :return: The created of this AttributeEvent.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created: datetime):
        """Sets the created of this AttributeEvent.


        :param created: The created of this AttributeEvent.
        :type created: datetime
        """

        self._created = created

    @property
    def etag(self) -> str:
        """Gets the etag of this AttributeEvent.


        :return: The etag of this AttributeEvent.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag: str):
        """Sets the etag of this AttributeEvent.


        :param etag: The etag of this AttributeEvent.
        :type etag: str
        """

        self._etag = etag

    @property
    def links(self) -> Links:
        """Gets the links of this AttributeEvent.


        :return: The links of this AttributeEvent.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this AttributeEvent.


        :param links: The links of this AttributeEvent.
        :type links: Links
        """

        self._links = links

    @property
    def meta_attribute_event(self) -> MetaAttributeEvent:
        """Gets the meta_attribute_event of this AttributeEvent.


        :return: The meta_attribute_event of this AttributeEvent.
        :rtype: MetaAttributeEvent
        """
        return self._meta_attribute_event

    @meta_attribute_event.setter
    def meta_attribute_event(self, meta_attribute_event: MetaAttributeEvent):
        """Sets the meta_attribute_event of this AttributeEvent.


        :param meta_attribute_event: The meta_attribute_event of this AttributeEvent.
        :type meta_attribute_event: MetaAttributeEvent
        """

        self._meta_attribute_event = meta_attribute_event
