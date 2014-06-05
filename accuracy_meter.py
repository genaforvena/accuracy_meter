# -*- coding: utf8 -*-
import sqlite3

DB_NAME = "corpus.db"


class AccuracyMeter(object):
    def __init__(self):
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

    def save_sentences_to_db(self, db_name):
        dbHelper = DbHelper(db_name)
        dbHelper.create_table()
        for (sentence_number, sentence) in enumerate(self.sentences):
            for line in sentence:
                dbHelper.write_line_to_db(sentence_number, line)



class DbHelper(object):
    def __init__(self, table_name):
        self.conn = sqlite3.connect(DB_NAME)
        self.table_name = table_name

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS %s (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, SENTENCE INT NOT NULL, FORM CHAR(50) NOT NULL, POSTAG CHAR(50) NOT NULL, HEAD INT, DEPREL CHAR(50));" % self.table_name
        self.conn.execute(query)

    def write_line_to_db(self, number_of_sentence, line_raw):
        line = line_raw.split("\t")
        query = 'INSERT INTO %s (SENTENCE, FORM, POSTAG, HEAD, DEPREL) VALUES (%s, "%s", "%s", %s, "%s");' % (self.table_name, number_of_sentence, line[0], line[1], line[2], line[3].rstrip())
        self.conn.cursor().execute(query)
        self.conn.commit()

    def get_sentence(self, sentence_number):
        query = "SELECT FORM, POSTAG, HEAD, DEPREL FROM %s WHERE SENTENCE=%s;" % (self.table_name, sentence_number)
        return self.conn.execute(query)

    def close(self):
        self.conn.close()

    if __name__ == "__main__":
        pass
