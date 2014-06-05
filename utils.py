# -*- coding: utf8 -*-
import sqlite3

from accuracy_meter import DB_NAME


class DbHelper(object):
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS %s (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, SENTENCE INT NOT NULL, FORM CHAR(50) NOT NULL, POSTAG CHAR(50) NOT NULL, HEAD INT, DEPREL CHAR(50));" % self.table_name
        self.conn.execute(query)

    def write_line_to_db(self, table, number_of_sentence, line_raw):
        line = line_raw.split("\t")
        query = 'INSERT INTO %s (SENTENCE, FORM, POSTAG, HEAD, DEPREL) VALUES (%s, "%s", "%s", %s, "%s");' % (
            table, number_of_sentence, line[0], line[1], line[2], line[3].rstrip())
        self.conn.cursor().execute(query)
        self.conn.commit()

    def get_sentence(self, table, sentence_number):
        query = "SELECT FORM, POSTAG, HEAD, DEPREL FROM %s WHERE SENTENCE=%s;" % (table, sentence_number)
        return self.conn.execute(query)

    def get_number_of_sentences(self, table):
        query = "SELECT MAX(SENTENCE) FROM %s;" % table
        return int(self.conn.execute(query))

    def close(self):
        self.conn.close()

    def open_and_close(self, function):
        def wrapper(function):
            self.conn = sqlite3.connect(DB_NAME)
            function()
            self.conn.close()

        return wrapper