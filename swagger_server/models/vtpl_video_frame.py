# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.source_type import SourceType  # noqa: F401,E501
from swagger_server import util


class VtplVideoFrame(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel_id: int=None, app_id: int=None, frame_id: int=None, time_stamp: int=None, fps: float=None, frame: object=None, is_first_frame: bool=False, is_end_of_stream: bool=False, type: SourceType=None, base_url: str=None, user: str=None, _pass: str=None):  # noqa: E501
        """VtplVideoFrame - a model defined in Swagger

        :param channel_id: The channel_id of this VtplVideoFrame.  # noqa: E501
        :type channel_id: int
        :param app_id: The app_id of this VtplVideoFrame.  # noqa: E501
        :type app_id: int
        :param frame_id: The frame_id of this VtplVideoFrame.  # noqa: E501
        :type frame_id: int
        :param time_stamp: The time_stamp of this VtplVideoFrame.  # noqa: E501
        :type time_stamp: int
        :param fps: The fps of this VtplVideoFrame.  # noqa: E501
        :type fps: float
        :param frame: The frame of this VtplVideoFrame.  # noqa: E501
        :type frame: object
        :param is_first_frame: The is_first_frame of this VtplVideoFrame.  # noqa: E501
        :type is_first_frame: bool
        :param is_end_of_stream: The is_end_of_stream of this VtplVideoFrame.  # noqa: E501
        :type is_end_of_stream: bool
        :param type: The type of this VtplVideoFrame.  # noqa: E501
        :type type: SourceType
        :param base_url: The base_url of this VtplVideoFrame.  # noqa: E501
        :type base_url: str
        :param user: The user of this VtplVideoFrame.  # noqa: E501
        :type user: str
        :param _pass: The _pass of this VtplVideoFrame.  # noqa: E501
        :type _pass: str
        """
        self.swagger_types = {
            'channel_id': int,
            'app_id': int,
            'frame_id': int,
            'time_stamp': int,
            'fps': float,
            'frame': object,
            'is_first_frame': bool,
            'is_end_of_stream': bool,
            'type': SourceType,
            'base_url': str,
            'user': str,
            '_pass': str
        }

        self.attribute_map = {
            'channel_id': 'channelId',
            'app_id': 'appId',
            'frame_id': 'frameId',
            'time_stamp': 'timeStamp',
            'fps': 'fps',
            'frame': 'frame',
            'is_first_frame': 'isFirstFrame',
            'is_end_of_stream': 'isEndOfStream',
            'type': 'type',
            'base_url': 'baseUrl',
            'user': 'user',
            '_pass': 'pass'
        }
        self._channel_id = channel_id
        self._app_id = app_id
        self._frame_id = frame_id
        self._time_stamp = time_stamp
        self._fps = fps
        self._frame = frame
        self._is_first_frame = is_first_frame
        self._is_end_of_stream = is_end_of_stream
        self._type = type
        self._base_url = base_url
        self._user = user
        self.__pass = _pass

    @classmethod
    def from_dict(cls, dikt) -> 'VtplVideoFrame':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vtplVideoFrame of this VtplVideoFrame.  # noqa: E501
        :rtype: VtplVideoFrame
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel_id(self) -> int:
        """Gets the channel_id of this VtplVideoFrame.


        :return: The channel_id of this VtplVideoFrame.
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id: int):
        """Sets the channel_id of this VtplVideoFrame.


        :param channel_id: The channel_id of this VtplVideoFrame.
        :type channel_id: int
        """

        self._channel_id = channel_id

    @property
    def app_id(self) -> int:
        """Gets the app_id of this VtplVideoFrame.


        :return: The app_id of this VtplVideoFrame.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: int):
        """Sets the app_id of this VtplVideoFrame.


        :param app_id: The app_id of this VtplVideoFrame.
        :type app_id: int
        """

        self._app_id = app_id

    @property
    def frame_id(self) -> int:
        """Gets the frame_id of this VtplVideoFrame.


        :return: The frame_id of this VtplVideoFrame.
        :rtype: int
        """
        return self._frame_id

    @frame_id.setter
    def frame_id(self, frame_id: int):
        """Sets the frame_id of this VtplVideoFrame.


        :param frame_id: The frame_id of this VtplVideoFrame.
        :type frame_id: int
        """

        self._frame_id = frame_id

    @property
    def time_stamp(self) -> int:
        """Gets the time_stamp of this VtplVideoFrame.


        :return: The time_stamp of this VtplVideoFrame.
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: int):
        """Sets the time_stamp of this VtplVideoFrame.


        :param time_stamp: The time_stamp of this VtplVideoFrame.
        :type time_stamp: int
        """

        self._time_stamp = time_stamp

    @property
    def fps(self) -> float:
        """Gets the fps of this VtplVideoFrame.


        :return: The fps of this VtplVideoFrame.
        :rtype: float
        """
        return self._fps

    @fps.setter
    def fps(self, fps: float):
        """Sets the fps of this VtplVideoFrame.


        :param fps: The fps of this VtplVideoFrame.
        :type fps: float
        """

        self._fps = fps

    @property
    def frame(self) -> object:
        """Gets the frame of this VtplVideoFrame.


        :return: The frame of this VtplVideoFrame.
        :rtype: object
        """
        return self._frame

    @frame.setter
    def frame(self, frame: object):
        """Sets the frame of this VtplVideoFrame.


        :param frame: The frame of this VtplVideoFrame.
        :type frame: object
        """

        self._frame = frame

    @property
    def is_first_frame(self) -> bool:
        """Gets the is_first_frame of this VtplVideoFrame.


        :return: The is_first_frame of this VtplVideoFrame.
        :rtype: bool
        """
        return self._is_first_frame

    @is_first_frame.setter
    def is_first_frame(self, is_first_frame: bool):
        """Sets the is_first_frame of this VtplVideoFrame.


        :param is_first_frame: The is_first_frame of this VtplVideoFrame.
        :type is_first_frame: bool
        """

        self._is_first_frame = is_first_frame

    @property
    def is_end_of_stream(self) -> bool:
        """Gets the is_end_of_stream of this VtplVideoFrame.


        :return: The is_end_of_stream of this VtplVideoFrame.
        :rtype: bool
        """
        return self._is_end_of_stream

    @is_end_of_stream.setter
    def is_end_of_stream(self, is_end_of_stream: bool):
        """Sets the is_end_of_stream of this VtplVideoFrame.


        :param is_end_of_stream: The is_end_of_stream of this VtplVideoFrame.
        :type is_end_of_stream: bool
        """

        self._is_end_of_stream = is_end_of_stream

    @property
    def type(self) -> SourceType:
        """Gets the type of this VtplVideoFrame.


        :return: The type of this VtplVideoFrame.
        :rtype: SourceType
        """
        return self._type

    @type.setter
    def type(self, type: SourceType):
        """Sets the type of this VtplVideoFrame.


        :param type: The type of this VtplVideoFrame.
        :type type: SourceType
        """

        self._type = type

    @property
    def base_url(self) -> str:
        """Gets the base_url of this VtplVideoFrame.


        :return: The base_url of this VtplVideoFrame.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url: str):
        """Sets the base_url of this VtplVideoFrame.


        :param base_url: The base_url of this VtplVideoFrame.
        :type base_url: str
        """

        self._base_url = base_url

    @property
    def user(self) -> str:
        """Gets the user of this VtplVideoFrame.


        :return: The user of this VtplVideoFrame.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this VtplVideoFrame.


        :param user: The user of this VtplVideoFrame.
        :type user: str
        """

        self._user = user

    @property
    def _pass(self) -> str:
        """Gets the _pass of this VtplVideoFrame.


        :return: The _pass of this VtplVideoFrame.
        :rtype: str
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass: str):
        """Sets the _pass of this VtplVideoFrame.


        :param _pass: The _pass of this VtplVideoFrame.
        :type _pass: str
        """

        self.__pass = _pass
