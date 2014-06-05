# -*- coding: utf8 -*-
from twisted.test.myrebuilder1 import A
import unittest

from accuracy_meter import *

class AccuracyMeterTest(unittest.TestCase):
    expected_path = "test_data/expected.txt"
    now_path = "test_data/now.txt"

    def test_compareShouldReturn100PercentForExactMatch(self):
        meter = AccuracyMeter()
        result = meter.compare(self.expected_path, self.expected_path)

        self.assertEquals(1, result)

    def test_comparePartlyEqualFilesShouldReturnCorrectNumber(self):
        meter = AccuracyMeter()
        result = meter.compare(self.expected_path, self.now_path)

        self.assertEquals(0.75, result)