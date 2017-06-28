# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductCreationResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rejected_count=None, accepted_count=None, product_messages=None):
        """
        ProductCreationResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rejected_count': 'int',
            'accepted_count': 'int',
            'product_messages': 'list[ProductMessage]'
        }

        self.attribute_map = {
            'rejected_count': 'RejectedCount',
            'accepted_count': 'AcceptedCount',
            'product_messages': 'ProductMessages'
        }

        self._rejected_count = rejected_count
        self._accepted_count = accepted_count
        self._product_messages = product_messages

    @property
    def rejected_count(self):
        """
        Gets the rejected_count of this ProductCreationResult.

        :return: The rejected_count of this ProductCreationResult.
        :rtype: int
        """
        return self._rejected_count

    @rejected_count.setter
    def rejected_count(self, rejected_count):
        """
        Sets the rejected_count of this ProductCreationResult.

        :param rejected_count: The rejected_count of this ProductCreationResult.
        :type: int
        """

        self._rejected_count = rejected_count

    @property
    def accepted_count(self):
        """
        Gets the accepted_count of this ProductCreationResult.

        :return: The accepted_count of this ProductCreationResult.
        :rtype: int
        """
        return self._accepted_count

    @accepted_count.setter
    def accepted_count(self, accepted_count):
        """
        Sets the accepted_count of this ProductCreationResult.

        :param accepted_count: The accepted_count of this ProductCreationResult.
        :type: int
        """

        self._accepted_count = accepted_count

    @property
    def product_messages(self):
        """
        Gets the product_messages of this ProductCreationResult.
        Messages about the rejected products.

        :return: The product_messages of this ProductCreationResult.
        :rtype: list[ProductMessage]
        """
        return self._product_messages

    @product_messages.setter
    def product_messages(self, product_messages):
        """
        Sets the product_messages of this ProductCreationResult.
        Messages about the rejected products.

        :param product_messages: The product_messages of this ProductCreationResult.
        :type: list[ProductMessage]
        """

        self._product_messages = product_messages

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProductCreationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other