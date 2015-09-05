#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2

This module gets called from site.py,
sends query from SQL and returns data to display
'''

from flask import Blueprint, render_template, request, Response, redirect, url_for, send_from_directory
import csv
from beach import db


imp = Blueprint('impact', __name__, template_folder='/../templates')


@imp.route('/')
def home():
    title = ''
    paragraph = ['This page displays .....']

    return render_template('impact.html', title=title, paragraph=paragraph, data=None, active_page='impact')