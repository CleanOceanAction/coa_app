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
    years = set()
    item_categories = []
    for year, item_category in get_item_categories_for_all_years():
        years.add(year)
        item_categories.append(item_category)

    return render_template('impact.html', title=title, paragraph=paragraph, data=None, active_page='impact',
                           item_categories=item_categories, years=sorted(years))


def get_item_categories_for_all_years():
    """
    Returns the data for materials and categories for all years as a list of '--' delimited strings.
    :return list of tuples:
    """
    query = """
        select a.yr, concat(a.yr,'--',a.material,'--',a.category,'\t',cast(round(a.total/b.yr_total*100,2) as char),'%') as cnt
        from (
            select year(volunteer_date) as yr, material, category, sum(quantity) as total 
            from coa_summary_view 
            group by year(volunteer_date), category
        ) as a
        left join (
            select year(volunteer_date) as yr, sum(quantity) as yr_total 
            from coa_summary_view 
            group by yr
        ) as b 
        on a.yr = b.yr
    """
    result = db.fetch_data(query)
    return result
