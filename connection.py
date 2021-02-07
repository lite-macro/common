from pymongo import MongoClient
import sqlite3
import psycopg2
import pymysql
import pymongo
import pandas as pd
import os
import sys

if os.getenv('MY_PYTHON_PKG') not in sys.path:
    sys.path.append(os.getenv('MY_PYTHON_PKG'))
import syspath

import sqlCommand as sqlc
from common.env import SQLITE_DB, PG_HOST, MONGO_HOST, PG_PWD, MYSQL_PWD, MONGO_PWD, PG_PORT, MYSQL_PORT, MONGO_PORT, PG_USER, MYSQL_USER


def conn_local_lite(db: str) -> sqlc.conn_lite:
    return sqlite3.connect(f'{SQLITE_DB}/{db}')


def conn_local_pg(db: str) -> sqlc.conn_pg:
    host = PG_HOST
    if host == '':
        host = 'localhost'
    return psycopg2.connect(f'host={host} port={PG_PORT} dbname={db} user={PG_USER} password={PG_PWD}')


def conn_local_my(db: str) -> sqlc.conn_my:
    return pymysql.connect(host='localhost', port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PWD, db=db, charset='utf8')


mongo_host = MONGO_HOST
if mongo_host == '':
    mongo_host = 'localhost'

conn_local_mgo = MongoClient('{mongo_host}', MONGO_PORT)
