# -*- coding: utf-8 -*-
""" tests module
"""
import pytest
from covid19umbria import Covid19Umbria
from unittest.mock import patch


class MockRequestData:
    @staticmethod
    def json():
        return {"key": "value"}


def test_all_data():
    covid19 = Covid19Umbria()
    data = covid19.get_data()
    assert data is not None
    assert type(data) == list
    d = data[0]
    assert "data" in d
