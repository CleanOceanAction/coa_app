#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2

Reads beach.config.py and
loads config into dashboard object depends on web server
'''
from flask import Flask
import socket

from beach.config import Config
from beach.config import DevConfig
from beach.config import ProdConfig

application = Flask(__name__)

if socket.gethostname().lower() == Config.WEB_SERVER_PROD:
    application.config.from_object(ProdConfig)
else:
    application.config.from_object(DevConfig)

from beach.views.contribution import cont
from beach.views.impact import imp

application.register_blueprint(cont, url_prefix='/contribution')
application.register_blueprint(imp, url_prefix='/impact')