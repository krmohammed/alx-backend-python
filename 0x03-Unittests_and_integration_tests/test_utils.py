#!/usr/bin/env python3
"""Tests Cases for the function access_nested_map
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """tests for for right answers"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ["a"]), ({"a": 1}, ["a", "b"])])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence):
        """tests for KeyError Exceptions"""
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test for get_json function"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requets):
        """test get_json"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requets.return_value = mock_response
        mock_requets.assert_called_once()
        self.assertEqual(test_payload, get_json(test_url))


if __name__ == "__main__":
    unittest.main()
