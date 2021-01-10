# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from swagger_server.test import BaseTestCase


class TestEnginesController(BaseTestCase):
    """EnginesController integration test stubs"""

    def test_anpr_events_get(self):
        """Test case for anpr_events_get

        Get all anprEvents
        """
        query_string = [('where', 'where_example'),
                        ('sort', 'sort_example'),
                        ('max_results', 56),
                        ('embedded', 'embedded_example')]
        response = self.client.open(
            '/anprEvents',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_anpr_events_id_get(self):
        """Test case for anpr_events_id_get

        Get anprEvent by id
        """
        query_string = [('embedded', 'embedded_example')]
        response = self.client.open(
            '/anprEvents/{id}'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_anpr_events_post(self):
        """Test case for anpr_events_post

        Create an anprEvent
        """
        body = AnprEvent()
        response = self.client.open(
            '/anprEvents',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_attribute_events_get(self):
        """Test case for attribute_events_get

        Get all attributeEvents
        """
        query_string = [('where', 'where_example'),
                        ('sort', 'sort_example'),
                        ('max_results', 56),
                        ('embedded', 'embedded_example')]
        response = self.client.open(
            '/attributeEvents',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_attribute_events_id_get(self):
        """Test case for attribute_events_id_get

        Get attributeEvent by id
        """
        query_string = [('embedded', 'embedded_example')]
        response = self.client.open(
            '/attributeEvents/{id}'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_attribute_events_post(self):
        """Test case for attribute_events_post

        Create an attributeEvent
        """
        body = AttributeEvent()
        response = self.client.open(
            '/attributeEvents',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clips_get(self):
        """Test case for clips_get

        Get all unprocesed clips
        """
        response = self.client.open(
            '/clips',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clips_id_get(self):
        """Test case for clips_id_get

        Get clip by id
        """
        response = self.client.open(
            '/clips/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clips_post(self):
        """Test case for clips_post

        Create an unprocesed clip
        """
        body = Clip()
        response = self.client.open(
            '/clips',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engine_tasks_get(self):
        """Test case for engine_tasks_get

        Get all engineTasks
        """
        query_string = [('where', 'where_example'),
                        ('page', 56),
                        ('sort', 'sort_example'),
                        ('max_results', 56)]
        response = self.client.open(
            '/engineTasks',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engine_tasks_id_delete(self):
        """Test case for engine_tasks_id_delete

        Delete an engine task
        """
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/engineTasks/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engine_tasks_id_get(self):
        """Test case for engine_tasks_id_get

        Get engine task by id
        """
        response = self.client.open(
            '/engineTasks/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engine_tasks_id_patch(self):
        """Test case for engine_tasks_id_patch

        Patch an engine task
        """
        body = EngineTask()
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/engineTasks/{id}'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engine_tasks_post(self):
        """Test case for engine_tasks_post

        Create an engineTask
        """
        body = EngineTask()
        response = self.client.open(
            '/engineTasks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engines_get(self):
        """Test case for engines_get

        Get all engine details
        """
        query_string = [('page', 56),
                        ('where', 'where_example'),
                        ('max_results', 56)]
        response = self.client.open(
            '/engines',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engines_id_delete(self):
        """Test case for engines_id_delete

        Delete an engine
        """
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/engines/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engines_id_get(self):
        """Test case for engines_id_get

        Get engine by id
        """
        response = self.client.open(
            '/engines/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_engines_post(self):
        """Test case for engines_post

        Create an engine
        """
        body = Engine()
        response = self.client.open(
            '/engines',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_event_snaps_get(self):
        """Test case for event_snaps_get

        Get all eventSnaps
        """
        response = self.client.open(
            '/eventSnaps',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_event_snaps_id_get(self):
        """Test case for event_snaps_id_get

        Get eventSnap by id
        """
        response = self.client.open(
            '/eventSnaps/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_event_snaps_post(self):
        """Test case for event_snaps_post

        Create an eventSnap
        """
        body = Snap()
        response = self.client.open(
            '/eventSnaps',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_snaps_get(self):
        """Test case for snaps_get

        Get all unprocesed snaps
        """
        response = self.client.open(
            '/snaps',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_snaps_id_get(self):
        """Test case for snaps_id_get

        Get snap by id
        """
        response = self.client.open(
            '/snaps/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_snaps_post(self):
        """Test case for snaps_post

        Create a unprocesed snap
        """
        body = Snap()
        response = self.client.open(
            '/snaps',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_va_events_get(self):
        """Test case for va_events_get

        Get all vaEvents
        """
        query_string = [('where', 'where_example'),
                        ('sort', 'sort_example'),
                        ('max_results', 56),
                        ('embedded', 'embedded_example')]
        response = self.client.open(
            '/vaEvents',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_va_events_id_get(self):
        """Test case for va_events_id_get

        Get vaEvent by id
        """
        query_string = [('embedded', 'embedded_example')]
        response = self.client.open(
            '/vaEvents/{id}'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_va_events_post(self):
        """Test case for va_events_post

        Create an vaEvent
        """
        body = VaEvent()
        response = self.client.open(
            '/vaEvents',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
