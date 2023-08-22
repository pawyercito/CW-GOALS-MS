# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_get_single_goals_vendor import RequestGetSingleGoalsVendor  # noqa: E501
from swagger_server.models.response_get_single_goals_vendor import ResponseGetSingleGoalsVendor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetSingleGoalsVendorController(BaseTestCase):
    """GetSingleGoalsVendorController integration test stubs"""

    def test_get_single_goals_vendor(self):
        """Test case for get_single_goals_vendor

        Obtener un goalsVendor específico.
        """
        body = RequestGetSingleGoalsVendor()
        response = self.client.open(
            '/goalsVendor/getsingle',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
