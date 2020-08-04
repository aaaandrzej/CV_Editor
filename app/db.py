import sqlite3


def get_connection():
    conn = sqlite3.connect('CV_Editor.db')  # TODO tak o czy "../app/CV_Editor.db"?
    conn.row_factory = sqlite3.Row
    return conn
