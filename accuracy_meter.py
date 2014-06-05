# -*- coding: utf8 -*-

class AccuracyMeter(object):
    pass

class TabFileParser(object):
    def __init__(self):
        self.file_lines = None
        self.sentences = []

    def parse_sentences(self):
        sentence = []
        for line in self.file_lines:
            if line == "\n":
                self.sentences.append(sentence)
                sentence = []
            else:
                sentence.append(line)
        self.file_lines = None

    def read_lines(self, path):
        with open(path, "r") as f:
            self.file_lines = f.readlines()

if __name__ == "__main__":
    pass
