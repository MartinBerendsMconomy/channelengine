# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.product_api import ProductApi


class TestProductApi(unittest.TestCase):
    """ ProductApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.product_api.ProductApi()

    def tearDown(self):
        pass

    def test_product_acknowledge_data_changes(self):
        """
        Test case for product_acknowledge_data_changes

        Channel: Acknowledge Product Data Changes
        """
        pass

    def test_product_acknowledge_offer_changes(self):
        """
        Test case for product_acknowledge_offer_changes

        Channel: Acknowledge Product Offer Changes
        """
        pass

    def test_product_create(self):
        """
        Test case for product_create

        Merchant: Create Product
        """
        pass

    def test_product_delete(self):
        """
        Test case for product_delete

        Merchant: Delete Product
        """
        pass

    def test_product_get_by_merchant_product_no(self):
        """
        Test case for product_get_by_merchant_product_no

        Merchant: Get Product
        """
        pass

    def test_product_get_data_changes(self):
        """
        Test case for product_get_data_changes

        Channel: Get Product Data Changes
        """
        pass

    def test_product_get_offer_changes(self):
        """
        Test case for product_get_offer_changes

        Channel: Get Product Offer Changes
        """
        pass


if __name__ == '__main__':
    unittest.main()