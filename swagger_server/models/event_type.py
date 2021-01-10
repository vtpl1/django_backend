# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EventType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    FACEEVENT = "faceEvent"
    ATTRIBUTEEVENT = "attributeEvent"
    ANPREVENT = "anprEvent"
    NOSEATBELTEVENT = "noSeatBeltEvent"
    DRIVERONCALLEVENT = "driverOnCallEvent"
    PEOPLECOLLAPSINGEVENT = "peopleCollapsingEvent"
    CROWDFORMATIONEVENT = "crowdFormationEvent"
    CROWDDISPERSIONEVENT = "crowdDispersionEvent"
    CROWDABNORMALITYEVENT = "crowdAbnormalityEvent"
    ATCCSEVENT = "atccsEvent"
    NOHELMETEVENT = "noHelmetEvent"
    PEOPLEONROADEVENT = "peopleOnRoadEvent"
    VEHICLECONGESTIONEVENT = "vehicleCongestionEvent"
    INTRUSIONDETECTIONEDGEEVENT = "intrusionDetectionEdgeEvent"
    INDUSTRIALNOHELMETEVENT = "industrialNoHelmetEvent"
    INDUSTRIALNOAPRONEVENT = "industrialNoApronEvent"
    VAEVENT = "vaEvent"
    def __init__(self):  # noqa: E501
        """EventType - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'EventType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The eventType of this EventType.  # noqa: E501
        :rtype: EventType
        """
        return util.deserialize_model(dikt, cls)
