import sqlite3
from langchain.tools import Tool

conn = sqlite3.connect("db.sqlite")


def run_sqlite_query(query):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()
