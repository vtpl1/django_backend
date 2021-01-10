import connexion
import six

from swagger_server.models.anpr_event import AnprEvent  # noqa: E501
from swagger_server.models.anpr_events_response import AnprEventsResponse  # noqa: E501
from swagger_server.models.attribute_event import AttributeEvent  # noqa: E501
from swagger_server.models.attribute_events_response import AttributeEventsResponse  # noqa: E501
from swagger_server.models.clip import Clip  # noqa: E501
from swagger_server.models.clips_response import ClipsResponse  # noqa: E501
from swagger_server.models.default_response import DefaultResponse  # noqa: E501
from swagger_server.models.engine import Engine  # noqa: E501
from swagger_server.models.engine_task import EngineTask  # noqa: E501
from swagger_server.models.engine_tasks_response import EngineTasksResponse  # noqa: E501
from swagger_server.models.engines_response import EnginesResponse  # noqa: E501
from swagger_server.models.event_snaps_response import EventSnapsResponse  # noqa: E501
from swagger_server.models.snap import Snap  # noqa: E501
from swagger_server.models.snaps_response import SnapsResponse  # noqa: E501
from swagger_server.models.va_event import VaEvent  # noqa: E501
from swagger_server.models.va_events_response import VaEventsResponse  # noqa: E501
from swagger_server import util


def anpr_events_get(where=None, sort=None, max_results=None, embedded=None):  # noqa: E501
    """Get all anprEvents

    Get all anprEvents # noqa: E501

    :param where: The where clause takes a JSON as a string with one or many properties of the anprEvent model. Example:   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /anprEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /anprEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;}
    :type where: str
    :param sort: The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort anprEvents by startTimeStamp in eventDetails IN ASCEDING order, use /anprEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort anprEvents by startTimeStamp in eventDetails IN DECENDING order, use /anprEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING
    :type sort: str
    :param max_results: The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest anprEvent among whole anprEvents, use /anprEvents?maxResults&#x3D;1   * To limit anprEvents to 5, use /anprEvents?maxResults&#x3D;5
    :type max_results: int
    :param embedded: The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find anprEvents with eventSnap object. use /anprEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27;
    :type embedded: str

    :rtype: AnprEventsResponse
    """
    return 'do some magic!'


def anpr_events_id_get(id, embedded=None):  # noqa: E501
    """Get anprEvent by id

    Get anprEvent by id # noqa: E501

    :param id: Unique ID
    :type id: str
    :param embedded: The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find anprEvents with eventSnap object. use /anprEvents/{id}?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27;
    :type embedded: str

    :rtype: AnprEvent
    """
    return 'do some magic!'


def anpr_events_post(body=None):  # noqa: E501
    """Create an anprEvent

    Create an anprEvent. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = AnprEvent.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def attribute_events_get(where=None, sort=None, max_results=None, embedded=None):  # noqa: E501
    """Get all attributeEvents

    Get all attributeEvents # noqa: E501

    :param where: The where clause takes a JSON as a string with one or many properties of the attributeEvent model. Example:   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /attributeEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /attributeEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;}
    :type where: str
    :param sort: The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort attributeEvents by startTimeStamp in eventDetails IN ASCEDING order, use /attributeEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort attributeEvents by startTimeStamp in eventDetails IN DECENDING order, use /attributeEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING
    :type sort: str
    :param max_results: The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest attributeEvent among whole attributeEvents, use /attributeEvents?maxResults&#x3D;1   * To limit attributeEvents to 5, use /attributeEvents?maxResults&#x3D;5
    :type max_results: int
    :param embedded: The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find attributeEvents with eventSnap object. use /attributeEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27;
    :type embedded: str

    :rtype: AttributeEventsResponse
    """
    return 'do some magic!'


def attribute_events_id_get(id, embedded=None):  # noqa: E501
    """Get attributeEvent by id

    Get attributeEvent by id # noqa: E501

    :param id: Unique ID
    :type id: str
    :param embedded: The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find attributeEvents with eventSnap object. use /attributeEvents/{id}?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27;
    :type embedded: str

    :rtype: AttributeEvent
    """
    return 'do some magic!'


def attribute_events_post(body=None):  # noqa: E501
    """Create an attributeEvent

    Create an attributeEvent. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = AttributeEvent.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def clips_get():  # noqa: E501
    """Get all unprocesed clips

    Get all unprocesed clips # noqa: E501


    :rtype: ClipsResponse
    """
    return 'do some magic!'


def clips_id_get(id):  # noqa: E501
    """Get clip by id

    Get clip by id # noqa: E501

    :param id: Unique ID
    :type id: str

    :rtype: Clip
    """
    return 'do some magic!'


def clips_post(body=None):  # noqa: E501
    """Create an unprocesed clip

    Create an unprocesed clip # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = Clip.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def engine_tasks_get(where=None, page=None, sort=None, max_results=None):  # noqa: E501
    """Get all engineTasks

    Get all engineTasks details # noqa: E501

    :param where: The where clause takes a JSON as a string with one or many properties of the engineTask model. Example:   * To find engineTasks with capbilitiesType equal 211 and sourceId equal \&quot;4\&quot;, use /engineTasks?where&#x3D;{\&quot;capbilitiesType\&quot;:322,\&quot;source.sourceId\&quot;:\&quot;4\&quot;}   * To find engineTasks with destination.extras.value equal \&quot;1553774721506487\&quot;, use /engineTasks?where&#x3D;{\&quot;destination.extras.value\&quot;:\&quot;1553774721506487\&quot;}
    :type where: str
    :param page: The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engines?page&#x3D;4
    :type page: int
    :param sort: The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTasks?sort&#x3D;created   * To sort engineTasks by created IN DECENDING order, use /engineTasks?sort&#x3D;-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING
    :type sort: str
    :param max_results: The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTasks?maxResults&#x3D;1   * To limit engineTasks to 2, use /engineTasks?maxResults&#x3D;2
    :type max_results: int

    :rtype: EngineTasksResponse
    """
    return 'do some magic!'


def engine_tasks_id_delete(id, if_match):  # noqa: E501
    """Delete an engine task

    Delete an engine task # noqa: E501

    :param id: Unique ID
    :type id: str
    :param if_match: 
    :type if_match: str

    :rtype: None
    """
    return 'do some magic!'


def engine_tasks_id_get(id):  # noqa: E501
    """Get engine task by id

    Get engine task for a given id # noqa: E501

    :param id: Unique ID
    :type id: str

    :rtype: EngineTask
    """
    return 'do some magic!'


def engine_tasks_id_patch(id, if_match, body=None):  # noqa: E501
    """Patch an engine task

    Patch an engine task. Submit an object with one or more properties of the engineTask model. &#x27;Ex. {\&quot;capbilitiesType\&quot;: [211, 206]} or {\&quot;capbilitiesType\&quot;: [211, 206], \&quot;source\&quot;: {\&quot;sourceId\&quot;:\&quot;\&quot;, .....}}&#x27; # noqa: E501

    :param id: Unique ID
    :type id: str
    :param if_match: 
    :type if_match: str
    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = EngineTask.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def engine_tasks_post(body=None):  # noqa: E501
    """Create an engineTask

    Create a engineTasks. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = EngineTask.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def engines_get(page=None, where=None, max_results=None):  # noqa: E501
    """Get all engine details

    Get all engine details # noqa: E501

    :param page: The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /engines?page&#x3D;4
    :type page: int
    :param where: The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /engines?where&#x3D;{\&quot;capabilities\&quot;:{\&quot;$in\&quot;:[206,211]}}
    :type where: str
    :param max_results: The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first registeredFace among all registeredFaces, use /engines?maxResults&#x3D;1   * To limit registeredFaces to 5, use /engines?maxResults&#x3D;5
    :type max_results: int

    :rtype: EnginesResponse
    """
    return 'do some magic!'


def engines_id_delete(id, if_match):  # noqa: E501
    """Delete an engine

    Delete an engine # noqa: E501

    :param id: Unique ID
    :type id: str
    :param if_match: 
    :type if_match: str

    :rtype: None
    """
    return 'do some magic!'


def engines_id_get(id):  # noqa: E501
    """Get engine by id

    Get engine details for a given id # noqa: E501

    :param id: Unique ID
    :type id: str

    :rtype: Engine
    """
    return 'do some magic!'


def engines_post(body=None):  # noqa: E501
    """Create an engine

    Create an engine. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = Engine.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def event_snaps_get():  # noqa: E501
    """Get all eventSnaps

    Get all eventSnaps # noqa: E501


    :rtype: EventSnapsResponse
    """
    return 'do some magic!'


def event_snaps_id_get(id):  # noqa: E501
    """Get eventSnap by id

    Get eventSnap by id # noqa: E501

    :param id: Unique ID
    :type id: str

    :rtype: Snap
    """
    return 'do some magic!'


def event_snaps_post(body=None):  # noqa: E501
    """Create an eventSnap

    Create an eventSnap. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = Snap.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def snaps_get():  # noqa: E501
    """Get all unprocesed snaps

    Get all unprocesed snaps # noqa: E501


    :rtype: SnapsResponse
    """
    return 'do some magic!'


def snaps_id_get(id):  # noqa: E501
    """Get snap by id

    Get snap by id # noqa: E501

    :param id: Unique ID
    :type id: str

    :rtype: Snap
    """
    return 'do some magic!'


def snaps_post(body=None):  # noqa: E501
    """Create a unprocesed snap

    Create an unprocesed snap # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = Snap.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def va_events_get(where=None, sort=None, max_results=None, embedded=None):  # noqa: E501
    """Get all vaEvents

    Get all vaEvents # noqa: E501

    :param where: The where clause takes a JSON as a string with one or many properties of the vaEvent model. Example:   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /vaEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /vaEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;}
    :type where: str
    :param sort: The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort vaEvents by startTimeStamp in eventDetails IN ASCEDING order, use /vaEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort vaEvents by startTimeStamp in eventDetails IN DECENDING order, use /vaEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING
    :type sort: str
    :param max_results: The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest vaEvent among whole vaEvents, use /vaEvents?maxResults&#x3D;1   * To limit vaEvents to 5, use /vaEvents?maxResults&#x3D;5
    :type max_results: int
    :param embedded: The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find vaEvents with eventSnap object. use /vaEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27;
    :type embedded: str

    :rtype: VaEventsResponse
    """
    return 'do some magic!'


def va_events_id_get(id, embedded=None):  # noqa: E501
    """Get vaEvent by id

    Get vaEvent by id # noqa: E501

    :param id: Unique ID
    :type id: str
    :param embedded: The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find vaEvents with eventSnap object. use /vaEvents/{id}?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27;
    :type embedded: str

    :rtype: VaEvent
    """
    return 'do some magic!'


def va_events_post(body=None):  # noqa: E501
    """Create an vaEvent

    Create an vaEvent. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DefaultResponse
    """
    if connexion.request.is_json:
        body = VaEvent.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
