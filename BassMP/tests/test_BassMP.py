#!/usr/bin/env python

"""Tests for `BassMP` package."""

import pytest


from BassMPBase import BassMPBase


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

import unittest
import numpy as np
import pandas as pd
from BassMP import BassMP

class TestBassOLSMP(unittest.TestCase):
    def setUp(self):
        # Create a sample dataset for testing
        data = pd.DataFrame({
            'Time': [1, 2, 3, 4, 5],
            'Sales': [10, 15, 20, 25, 30]
        })
        self.model = BassOLSMP(data)

    def test_calculate_bass_model(self):
        # Test the calculate_bass_model function
        rate_of_change = self.model.calculate_bass_model(0.03, 0.1, 2)
        self.assertAlmostEqual(rate_of_change, 0.007478178)

    def test_calculate_parameters(self):
        # Test the calculate_parameters method
        self.model.fit()
        maximum_adopters, innovation_coefficient, imitation_coefficient = self.model.calculate_parameters()
        self.assertAlmostEqual(maximum_adopters, 45.0)
        self.assertAlmostEqual(innovation_coefficient, 0.028888888)
        self.assertAlmostEqual(imitation_coefficient, -0.644444444)

    def test_visualize_forecast(self):
        # Test the visualize_forecast method
        self.model.fit()
        self.model.calculate_parameters()
        self.model.predict()
        self.model.visualize_forecast()  # Manually check the generated plot

if __name__ == '__main__':
    unittest.main()
