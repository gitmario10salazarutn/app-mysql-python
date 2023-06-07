# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:32 2023

@author: Mario
"""

import mysql.connector as conn
from decouple import config


def connect_postgresql(hostname, dbname, username, password):
    try:
        config = {
            'user': username,
            'password': password,
            'host': hostname,
            'database': dbname,
            'raise_on_warnings': True
        }
        conn_post = conn.connect(**config)
        print(conn_post)
        return conn_post
    except Exception as e:
        print("Ocurrió un error al conectar a MySQL: ", e)
        raise Exception(e)


def get_connection():
    try:
        connection = connect_postgresql(
            config('HOST_NAME'),
            config('DATABASE'),
            config('USER_NAME'),
            config('PASSWORD')
        )
        return connection
    except Exception as ex:
        raise Exception(ex)
