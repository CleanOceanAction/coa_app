#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2
'''

import pymysql
from beach import application

def db_conn():
    conn = pymysql.connect(
        host=application.config['DB_SERVER'],
        port=application.config['DB_PORT'],
        user=application.config['DB_USERNAME'],
        passwd=application.config['DB_PASSWORD'],
        db=application.config['DB_DATABASE'],
        charset='utf8',
        use_unicode='true'
    )
    return conn

def fetch_data(query):
    conn=db_conn()
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def insert(query):
    conn=db_conn()
    cur = conn.cursor()
    cur.execute(query)
    cur.commit()
    cur.close()
    conn.close()