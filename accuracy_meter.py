# -*- coding: utf8 -*-
import utils

DB_NAME = "corpus.db"


class AccuracyMeter(object):
    pass

    def compare(self):
        pass


class TabFileParser(object):
    def __init__(self):
        self.sentences = []

    def parse_sentences(self, path):
        with open(path, "r") as f:
            file_lines = f.readlines()
            last_element = file_lines[-1]
            sentence = []
            for line in file_lines:
                if line == "\n":
                    self.sentences.append(sentence)
                    sentence = []
                elif line == last_element:
                    sentence.append(line)
                    self.sentences.append(sentence)
                else:
                    sentence.append(line)

    def save_sentences_to_db(self, table_name):
        dbhelper = DbHelper()
        dbhelper.create_table()
        for (sentence_number, sentence) in enumerate(self.sentences):
            for line in sentence:
                dbhelper.write_line_to_db(table_name, sentence_number, line)
        dbhelper.close()


class SentenceComparator(object):
    # This should be much more complex.
    # Acts more like a stub for now
    def __init__(self):
        self.matches = 0
        self.checked = 0

    def compare(self, table1, table2):
        dbhelper = DbHelper()
        for i in range(dbhelper.get_number_of_sentences(table1)):
            self._compare_sentences()
        return self._get_percentage()

    def _get_percentage(self):
        return long(self.matches / self.checked)

    def _compare_sentences(self):
        pass


if __name__ == "__main__":
    pass
