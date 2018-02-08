# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.4.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from channelengine_api_client.models.product_creation_result import ProductCreationResult  # noqa: F401,E501


class SingleOfProductCreationResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'content': 'ProductCreationResult',
        'status_code': 'int',
        'success': 'bool',
        'message': 'str',
        'validation_errors': 'dict(str, list[str])'
    }

    attribute_map = {
        'content': 'Content',
        'status_code': 'StatusCode',
        'success': 'Success',
        'message': 'Message',
        'validation_errors': 'ValidationErrors'
    }

    def __init__(self, content=None, status_code=None, success=None, message=None, validation_errors=None):  # noqa: E501
        """SingleOfProductCreationResult - a model defined in Swagger"""  # noqa: E501

        self._content = None
        self._status_code = None
        self._success = None
        self._message = None
        self._validation_errors = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if status_code is not None:
            self.status_code = status_code
        if success is not None:
            self.success = success
        if message is not None:
            self.message = message
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def content(self):
        """Gets the content of this SingleOfProductCreationResult.  # noqa: E501


        :return: The content of this SingleOfProductCreationResult.  # noqa: E501
        :rtype: ProductCreationResult
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SingleOfProductCreationResult.


        :param content: The content of this SingleOfProductCreationResult.  # noqa: E501
        :type: ProductCreationResult
        """

        self._content = content

    @property
    def status_code(self):
        """Gets the status_code of this SingleOfProductCreationResult.  # noqa: E501


        :return: The status_code of this SingleOfProductCreationResult.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this SingleOfProductCreationResult.


        :param status_code: The status_code of this SingleOfProductCreationResult.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def success(self):
        """Gets the success of this SingleOfProductCreationResult.  # noqa: E501


        :return: The success of this SingleOfProductCreationResult.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SingleOfProductCreationResult.


        :param success: The success of this SingleOfProductCreationResult.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def message(self):
        """Gets the message of this SingleOfProductCreationResult.  # noqa: E501


        :return: The message of this SingleOfProductCreationResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SingleOfProductCreationResult.


        :param message: The message of this SingleOfProductCreationResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def validation_errors(self):
        """Gets the validation_errors of this SingleOfProductCreationResult.  # noqa: E501


        :return: The validation_errors of this SingleOfProductCreationResult.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this SingleOfProductCreationResult.


        :param validation_errors: The validation_errors of this SingleOfProductCreationResult.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._validation_errors = validation_errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SingleOfProductCreationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
