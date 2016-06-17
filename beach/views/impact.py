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
    itemcategory = get_itemcategory()
    return render_template('impact.html', title=title, paragraph=paragraph, data=None, active_page='impact',
                           itemcategory=itemcategory)


def get_itemcategory():
    """
    Get all the possible possible inputs for pull down
    """
    query = """
        select concat(material,'--',category
        ,'\t',cast(round(sum(quantity)/(select sum(quantity) from volunteer_info)*100,2) as char)
        ,'%')as cnt
        from volunteer_info a
        join  item b
        on a.item_id=b.item_id
        group by material,b.category
    """
    itemcategory = db.fetch_data(query)
    return itemcategory
