# -*- coding: utf8 -*-
import os
import unittest

from accuracy_meter import *

expected_path = "test_data/expected.txt"
now_path = "test_data/now.txt"


class AccuracyMeterTest(unittest.TestCase):
    def test_compareShouldReturn100PercentForExactMatch(self):
        meter = AccuracyMeter()
        result = meter.compare(expected_path, expected_path)

        self.assertEquals(1, result)

    def test_comparePartlyEqualFilesShouldReturnCorrectNumber(self):
        meter = AccuracyMeter()
        result = meter.compare(expected_path, now_path)

        self.assertEquals(0.75, result)

    def tearDown(self):
        from accuracy_meter import DB_NAME

        try:
            os.remove(DB_NAME)
        except OSError:
            pass


class TabFileParserTest(unittest.TestCase):
    expected_first_sentence = ["Ведь\tPART\t7\tогранич\n", "текст\tS.m.nom.sg\t7\tпредик\n",
                               "закона\tS.gen.m.sg\t2\tквазиагент\n", "в\tPR\t7\tобст\n",
                               "этом\tA.m.prep.sg\t6\tопред\n",
                               "случае\tS.m.prep.sg\t4\tпредл\n", "остается\tV.3p.real.sg\t0\tROOT\n",
                               "прежним\tA.ins.m.sg\t7\tприсвяз\n"]
    expected_last_sentence = ["Как\tADV\t2\tобст\n", "повернешь\tV.2p.real.sg\t0\tROOT\n"]

    def test_parseSentencesFirstSentence(self):
        parser = TabFileParser()
        parser.parse_sentences(expected_path)

        self.assertEquals(self.expected_first_sentence, parser.sentences[0])

    def test_parseSentencesLastSentence(self):
        parser = TabFileParser()
        parser.parse_sentences(expected_path)

        self.assertEquals(self.expected_last_sentence, parser.sentences[-1])


