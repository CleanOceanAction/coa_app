#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2
'''

import pandas as pd
import pymysql
from beach import application


def fetch_data(query):
    conn = pymysql.connect(host=application.config['DB_SERVER'],
                           port=application.config['DB_PORT'],
                           user=application.config['DB_USERNAME'],
                           passwd=application.config['DB_PASSWORD'],
                           db=application.config['DB_DATABASE'],
                           charset='utf8',
                           use_unicode='true')
    return pd.read_sql(query, conn)


def insert(df, table):
    pass
