# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.response_delete_goals_vendor import ResponseDeleteGoalsVendor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDeleteGoalsVendorController(BaseTestCase):
    """DeleteGoalsVendorController integration test stubs"""

    def test_delete_goals_vendor(self):
        """Test case for delete_goals_vendor

        Eliminar goalsVendor.
        """
        response = self.client.open(
            '/goalsVendor/delete/{id_goal}'.format(id_goal=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
