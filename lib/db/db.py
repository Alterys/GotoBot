import sqlite3 as sq
from os.path import isfile

BUILD_PATH = "./data/db/build.sql"

base = sq.connect("data/db/server.db")
cur = base.cursor()


def get_prefix(guild_id):
    cur.execute("SELECT prefix FROM guilds WHERE guild_id == ?", (guild_id, ))
    return list(cur.fetchone())[0]


def commit():
    base.commit()


def execute(command, *values):
    cur.execute(command, tuple(values))


def record(command, *values):
    cur.execute(command, tuple(values))
    return cur.fetchone()


def records(command, *values):
    cur.execute(command, tuple(values))
    return cur.fetchall()


def insert(command):
    cur.execute(command)


def build():
    if isfile(BUILD_PATH):
        with open(BUILD_PATH, 'r', encoding="UTF-8") as script:
            cur.execute(script.read())
        commit()
