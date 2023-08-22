# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_edit_goals_vendor import RequestEditGoalsVendor  # noqa: E501
from swagger_server.models.response_edit_goals_vendor import ResponseEditGoalsVendor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUpdateGoalsVendorController(BaseTestCase):
    """UpdateGoalsVendorController integration test stubs"""

    def test_edit_goals_vendor(self):
        """Test case for edit_goals_vendor

        Actualizar goalsVendor.
        """
        body = RequestEditGoalsVendor()
        response = self.client.open(
            '/goalsVendor/{id_goal}'.format(id_goal=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
