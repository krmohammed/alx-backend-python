#!/usr/bin/env python3
"""Test Case for utils.access_nested_map"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ({}, ("a",), "KeyError: 'a'"),
            ({"a": 1}, ("a", "b"), "KeyError: 'b'")
        ]
    )
    def test_access_nested_map_exeception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)
            self.assertEqual(str(exc.exception), expected)
