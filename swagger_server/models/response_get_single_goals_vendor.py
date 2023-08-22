# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.goals_vendor_data import GoalsVendorData  # noqa: F401,E501
from swagger_server import util


class ResponseGetSingleGoalsVendor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None, message: str=None,channel: str=None, externalTransactionId: str=None, internalTransactionId: str=None, data: GoalsVendorData=None):  # noqa: E501
        """ResponseGetSingleGoalsVendor - a model defined in Swagger

        :param channel: The channel of this ResponseGetSingleGoalsVendor.  # noqa: E501
        :type channel: str
        :param externalTransactionId: The externalTransactionId of this ResponseGetSingleGoalsVendor.  # noqa: E501
        :type externalTransactionId: str
        :param internalTransactionId: The internalTransactionId of this ResponseGetSingleGoalsVendor.  # noqa: E501
        :type internalTransactionId: str
        :param data: The data of this ResponseGetSingleGoalsVendor.  # noqa: E501
        :type data: GoalsVendorData
        """
        self.swagger_types = {
            'code': str,
            'message': str,
            'channel': str,
            'externalTransactionId': str,
            'internalTransactionId': str,
            'data': GoalsVendorData
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'channel': 'channel',
            'externalTransactionId': 'externalTransactionId',
            'internalTransactionId': 'internalTransactionId',
            'data': 'data'
        }
        self._code = code
        self._message = message
        self._channel = channel
        self._externalTransactionId = externalTransactionId
        self._internalTransactionId = internalTransactionId
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseGetSingleGoalsVendor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseGetSingleGoalsVendor of this ResponseGetSingleGoalsVendor.  # noqa: E501
        :rtype: ResponseGetSingleGoalsVendor
        """
        return util.deserialize_model(dikt, cls)
    


    @property
    def code(self) -> str:
        """Gets the code of this ResponseGetSingleCommercialCondition.


        :return: The code of this ResponseGetSingleCommercialCondition.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ResponseGetSingleCommercialCondition.


        :param code: The code of this ResponseGetSingleCommercialCondition.
        :type code: str
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ResponseGetSingleCommercialCondition.


        :return: The message of this ResponseGetSingleCommercialCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseGetSingleCommercialCondition.


        :param message: The message of this ResponseGetSingleCommercialCondition.
        :type message: str
        """

        self._message = message

    @property
    def channel(self) -> str:
        """Gets the channel of this ResponseGetSingleGoalsVendor.


        :return: The channel of this ResponseGetSingleGoalsVendor.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this ResponseGetSingleGoalsVendor.


        :param channel: The channel of this ResponseGetSingleGoalsVendor.
        :type channel: str
        """

        self._channel = channel

    @property
    def externalTransactionId(self) -> str:
        """Gets the externalTransactionId of this ResponseGetSingleGoalsVendor.


        :return: The externalTransactionId of this ResponseGetSingleGoalsVendor.
        :rtype: str
        """
        return self._externalTransactionId

    @externalTransactionId.setter
    def externalTransactionId(self, externalTransactionId: str):
        """Sets the externalTransactionId of this ResponseGetSingleGoalsVendor.


        :param externalTransactionId: The externalTransactionId of this ResponseGetSingleGoalsVendor.
        :type externalTransactionId: str
        """

        self._externalTransactionId = externalTransactionId

    @property
    def internalTransactionId(self) -> str:
        """Gets the internalTransactionId of this ResponseGetSingleGoalsVendor.


        :return: The internalTransactionId of this ResponseGetSingleGoalsVendor.
        :rtype: str
        """
        return self._internalTransactionId

    @internalTransactionId.setter
    def internalTransactionId(self, internalTransactionId: str):
        """Sets the internalTransactionId of this ResponseGetSingleGoalsVendor.


        :param internalTransactionId: The internalTransactionId of this ResponseGetSingleGoalsVendor.
        :type internalTransactionId: str
        """

        self._internalTransactionId = internalTransactionId

    @property
    def data(self) -> GoalsVendorData:
        """Gets the data of this ResponseGetSingleGoalsVendor.


        :return: The data of this ResponseGetSingleGoalsVendor.
        :rtype: GoalsVendorData
        """
        return self._data

    @data.setter
    def data(self, data: GoalsVendorData):
        """Sets the data of this ResponseGetSingleGoalsVendor.


        :param data: The data of this ResponseGetSingleGoalsVendor.
        :type data: GoalsVendorData
        """

        self._data = data