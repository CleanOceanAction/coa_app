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

    counties = set()
    total_debris_per_county_by_year = []
    for county, county_year_total in get_totals_per_county_by_year():
        counties.add(county)
        total_debris_per_county_by_year.append(county_year_total)

    return render_template('impact.html', 
                            title=title, 
                            paragraph=paragraph, 
                            data=None, 
                            active_page='impact',
                            item_categories=item_categories, 
                            years=sorted(years), 
                            counties=sorted(counties),
                            total_debris_per_county_by_year=total_debris_per_county_by_year)


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
            select year(volunteer_date) as yr, county, sum(quantity) as yr_total 
            from coa_summary_view 
            group by yr
        ) as b 
        on a.yr = b.yr
    """
    result = db.fetch_data(query)
    return result

def get_totals_per_county_by_year():
    """
    Returns the total debris collected in each county by year.
    Return format <county>, <county--year \t total debris>.
    """
    query = """
        select county, concat(county, '--', cast(year(volunteer_date) as char), '\t', cast(sum(quantity) as char)) as count 
        from coa_summary_view 
        group by year(volunteer_date), county;
    """
    result = db.fetch_data(query)
    return result
