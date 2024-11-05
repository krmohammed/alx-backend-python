#!/usr/bin/env python3
"""Tests"""
import unittest
import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path):
        """tests"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
