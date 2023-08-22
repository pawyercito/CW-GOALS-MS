# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_get_all_goals_vendor import RequestGetAllGoalsVendor  # noqa: E501
from swagger_server.models.response_get_all_goals_vendor import ResponseGetAllGoalsVendor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAllGoalsVendorController(BaseTestCase):
    """AllGoalsVendorController integration test stubs"""

    def test_get_all_goals_vendor(self):
        """Test case for get_all_goals_vendor

        Obtener todos los goalsVendor.
        """
        body = RequestGetAllGoalsVendor()
        response = self.client.open(
            '/goalsVendor/getall',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
