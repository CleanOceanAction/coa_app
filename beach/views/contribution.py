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
from datetime import datetime


cont = Blueprint('contribution', __name__, template_folder='/../templates')


@cont.route('/', methods=['GET', 'POST'])
def collected_items():

    if request.method == 'GET':
        title = "Please enter your contribution!"
        sites = get_sites()
        tls = get_tls()
        trash_items = get_trash_items()

        return render_template("contribution_input.html",
                               title=title,
                               sites=sites,
                               tls=tls,
                               trash_items=trash_items,
                               active_page='contribution')

    elif request.method == 'POST':
        title = "Thank you for your contribution!"
        return render_template("contribution_output.html",
                               title=title,
                               active_page='contribution')


@cont.route('/ajax')
def ajax():
    tls = get_tls()
    return Response(tls)

@cont.route('/admin')
def admin():
    sites = get_sites()
    tls = get_tls()
    return render_template("admin.html",
                            sites=sites,
                            tls=tls)

@cont.route('/addSite')
def addSite():
    if request.method == 'POST':
        sitename=request.form.items()[0][0]
        #query='insert into site'
        #db.insert(query)
        return ''

@cont.route('/updatedb', methods=['GET', 'POST'])
def updatedb():
    if request.method == 'POST':
        query = create_query(request.form)
        db.insert(query)
        return ''


@cont.route('/thank_you')
def thank_you():
    title = ""
    return render_template("contribution_output.html",
                           title=title,
                           active_page='contribution')


def get_sites():
    """
    Get all the possible possible inputs for pull down
    """
    query = "SELECT site_id, CONCAT(town, ', ', site_name) AS site_name FROM coa.site ORDER BY town, site_name;"
    sites = db.fetch_data(query)
    return sites


def get_tls():
    query = """
    SELECT
        team_id,
        captain_name
    FROM coa.team
    ORDER BY captain_name;
    """
    tls = [tl for tl in db.fetch_data(query)]
    return tls


def get_trash_items():
    query = """
  SELECT
        DISTINCT item_id,
        material,
        concat(category,', ', ifnull(item_name,'') ,'[',item_id,']') as category
    FROM coa.item;
    """
    items = db.fetch_data(query);

    trash_items = {}
    for item in items:
        item_id, parent, child = item
        if parent in trash_items:
            trash_items[parent].append(child)
            trash_items[parent] = sorted(trash_items[parent])

        else:
            trash_items[parent]=[child]

    return trash_items


def create_query(imd):
    table = 'coa_inputs'
    cols = ['site_id', 'group_captain', 'date', 'category', 'quantity', 'brand','updated_by','event_code']
    query = """
    insert into volunteer_record
    (site_id, team_id, volunteer_date, item_id, quantity, brand,updated_by,event_code)
    VALUES
    """


    print query


    reader = csv.reader(imd.items()[0][0].split('||'), delimiter='#')
    for row in reader:
        if row:
            print row[3]
            query += "(%s,%s,'%s',%s,%s,'%s','%s','%s')," % (
                row[0],
                row[1],
                datetime.strptime(row[2], '%m/%d/%Y').strftime("%Y-%m-%d"),
                row[3].split('[')[1].split(']')[0],
                row[4],
                row[5],
                row[6],
                row[7]
            )


    print query[:-1] + ';'
    return query[:-1] + ';'

