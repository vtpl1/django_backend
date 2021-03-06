# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server import util


class Clip(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, clip: str=None, clip_id: str=None, starp_time_stamp: int=None, end_time_stamp: int=None, updated: datetime=None, created: datetime=None, etag: str=None, links: Links=None):  # noqa: E501
        """Clip - a model defined in Swagger

        :param id: The id of this Clip.  # noqa: E501
        :type id: str
        :param clip: The clip of this Clip.  # noqa: E501
        :type clip: str
        :param clip_id: The clip_id of this Clip.  # noqa: E501
        :type clip_id: str
        :param starp_time_stamp: The starp_time_stamp of this Clip.  # noqa: E501
        :type starp_time_stamp: int
        :param end_time_stamp: The end_time_stamp of this Clip.  # noqa: E501
        :type end_time_stamp: int
        :param updated: The updated of this Clip.  # noqa: E501
        :type updated: datetime
        :param created: The created of this Clip.  # noqa: E501
        :type created: datetime
        :param etag: The etag of this Clip.  # noqa: E501
        :type etag: str
        :param links: The links of this Clip.  # noqa: E501
        :type links: Links
        """
        self.swagger_types = {
            'id': str,
            'clip': str,
            'clip_id': str,
            'starp_time_stamp': int,
            'end_time_stamp': int,
            'updated': datetime,
            'created': datetime,
            'etag': str,
            'links': Links
        }

        self.attribute_map = {
            'id': '_id',
            'clip': 'clip',
            'clip_id': 'clipId',
            'starp_time_stamp': 'starpTimeStamp',
            'end_time_stamp': 'endTimeStamp',
            'updated': 'updated',
            'created': 'created',
            'etag': 'etag',
            'links': 'links'
        }
        self._id = id
        self._clip = clip
        self._clip_id = clip_id
        self._starp_time_stamp = starp_time_stamp
        self._end_time_stamp = end_time_stamp
        self._updated = updated
        self._created = created
        self._etag = etag
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'Clip':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The clip of this Clip.  # noqa: E501
        :rtype: Clip
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Clip.


        :return: The id of this Clip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Clip.


        :param id: The id of this Clip.
        :type id: str
        """

        self._id = id

    @property
    def clip(self) -> str:
        """Gets the clip of this Clip.


        :return: The clip of this Clip.
        :rtype: str
        """
        return self._clip

    @clip.setter
    def clip(self, clip: str):
        """Sets the clip of this Clip.


        :param clip: The clip of this Clip.
        :type clip: str
        """

        self._clip = clip

    @property
    def clip_id(self) -> str:
        """Gets the clip_id of this Clip.


        :return: The clip_id of this Clip.
        :rtype: str
        """
        return self._clip_id

    @clip_id.setter
    def clip_id(self, clip_id: str):
        """Sets the clip_id of this Clip.


        :param clip_id: The clip_id of this Clip.
        :type clip_id: str
        """

        self._clip_id = clip_id

    @property
    def starp_time_stamp(self) -> int:
        """Gets the starp_time_stamp of this Clip.

        Unix timestamp from when clip is recorded  # noqa: E501

        :return: The starp_time_stamp of this Clip.
        :rtype: int
        """
        return self._starp_time_stamp

    @starp_time_stamp.setter
    def starp_time_stamp(self, starp_time_stamp: int):
        """Sets the starp_time_stamp of this Clip.

        Unix timestamp from when clip is recorded  # noqa: E501

        :param starp_time_stamp: The starp_time_stamp of this Clip.
        :type starp_time_stamp: int
        """

        self._starp_time_stamp = starp_time_stamp

    @property
    def end_time_stamp(self) -> int:
        """Gets the end_time_stamp of this Clip.

        Unix timestamp till when clip is recorded  # noqa: E501

        :return: The end_time_stamp of this Clip.
        :rtype: int
        """
        return self._end_time_stamp

    @end_time_stamp.setter
    def end_time_stamp(self, end_time_stamp: int):
        """Sets the end_time_stamp of this Clip.

        Unix timestamp till when clip is recorded  # noqa: E501

        :param end_time_stamp: The end_time_stamp of this Clip.
        :type end_time_stamp: int
        """

        self._end_time_stamp = end_time_stamp

    @property
    def updated(self) -> datetime:
        """Gets the updated of this Clip.


        :return: The updated of this Clip.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated: datetime):
        """Sets the updated of this Clip.


        :param updated: The updated of this Clip.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def created(self) -> datetime:
        """Gets the created of this Clip.


        :return: The created of this Clip.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created: datetime):
        """Sets the created of this Clip.


        :param created: The created of this Clip.
        :type created: datetime
        """

        self._created = created

    @property
    def etag(self) -> str:
        """Gets the etag of this Clip.


        :return: The etag of this Clip.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag: str):
        """Sets the etag of this Clip.


        :param etag: The etag of this Clip.
        :type etag: str
        """

        self._etag = etag

    @property
    def links(self) -> Links:
        """Gets the links of this Clip.


        :return: The links of this Clip.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this Clip.


        :param links: The links of this Clip.
        :type links: Links
        """

        self._links = links
