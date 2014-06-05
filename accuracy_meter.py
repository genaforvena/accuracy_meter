# -*- coding: utf8 -*-
from utils import DbHelper

DB_NAME = "corpus.db"


class AccuracyMeter(object):
    def __init__(self):
        self.tab_parser = TabFileParser()
        self.comparator = SentenceComparator()

    def process_file(self, file):
        db_name = file.split("/")[-1]
        self.tab_parser.parse_sentences(file)
        self.tab_parser.save_sentences_to_db(db_name)
        return db_name

    def compare(self, file1, file2):
        map(self.comparator.compare, map(self.process_file, [file1, file2]))


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
        dbhelper.create_table(table_name)
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
        self.checked = dbhelper.get_number_of_sentences(table1)
        for i in range(self.checked):
            if are_same(dbhelper.get_sentence(table1, i), dbhelper.get_sentence(table2, i)):
                self.matches += 1
        return self._get_percentage()

    def _get_percentage(self):
        return long(self.matches / self.checked)


def are_same(sentence1, sentence2):
    if sentence1 == sentence2:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
