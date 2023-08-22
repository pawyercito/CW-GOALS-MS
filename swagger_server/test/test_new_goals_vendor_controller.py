# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_new_goals_vendor import RequestNewGoalsVendor  # noqa: E501
from swagger_server.models.response_new_goals_vendor import ResponseNewGoalsVendor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNewGoalsVendorController(BaseTestCase):
    """NewGoalsVendorController integration test stubs"""

    def test_new_goals_vendor(self):
        """Test case for new_goals_vendor

        Crear un nuevo goalsVendor.
        """
        body = RequestNewGoalsVendor()
        response = self.client.open(
            '/goalsVendor/new',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
