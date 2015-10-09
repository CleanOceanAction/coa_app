#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2

This module gets called from site.py, 
sends query from SQL and returns data to display
'''

from flask import Blueprint, render_template, request, Response, redirect, url_for, send_from_directory,session
import csv
from beach import db
from datetime import datetime


cont = Blueprint('contribution', __name__, template_folder='/../templates')

'''
@cont.route('/', methods=['GET', 'POST'])
def collected_items():
    if request.method == 'GET':
        title = "Please enter your contribution!"
        sites = get_sites()
        tls = get_tls()
        trash_items = get_trash_items()
        updater=''
        eventcode=''
        print "contribution"
        print session
        if 'updater' in session:
            updater=session['updater']
        if 'eventcode' in session:
            eventcode=session['eventcode']
        return render_template("contribution_input.html",
                               title=title,
                               sites=sites,
                               tls=tls,
                               trash_items=trash_items,
                               updater=updater,
                               eventcode=eventcode,
                               active_page='contribution')

    elif request.method == 'POST':
        title = "Thank you for your contribution!"
        return render_template("contribution_output.html",
                               title=title,
                               active_page='contribution')
'''

def get_leaderboard():
    query = """
    SELECT updated_by,count(*) as cnt
    FROM coa.volunteer_record
    where updated_by<>"" and event_code<>""
    group by updated_by order by count(*) desc
    """
    lb=db.fetch_data(query)
    return lb

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
@cont.route('/leaderboard')
def leaderboard():
    lb=get_leaderboard()
    return render_template("leaderboard.html",
                            lb=lb)

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
        try:
            query = create_query(request.form)
            db.insert(query)
            return 'Your records have been successfully saved!'
        except:
            return "Your records failed in saving to db. Please make sure you have all fields filled properly!"


@cont.route('/thank_you')
def thank_you():
    title = "Your records have been successfully saved!"
    return render_template("contribution_output.html",
                           title=title,
                           active_page='contribution')

@cont.route('/saveuserinfo', methods=['GET', 'POST'])
def saveuserinfo():
    if request.method == 'POST':
        userinfo=request.form.items()[0][0].split('||')
        updater=userinfo[0]
        eventcode=userinfo[1]
        if len(updater)>=1 and len(eventcode)>=1:
            session['updater']=updater
            session['eventcode']=eventcode
            title = "Please enter your contribution!"
            sites = get_sites()
            tls = get_tls()
            trash_items = get_trash_items()
            return render_template("contribution_input.html",
                                   title=title,
                                   sites=sites,
                                   tls=tls,
                                   trash_items=trash_items,
                                   updater=updater,
                                   eventcode=eventcode,
                                   active_page='contribution')
        else:
            return render_template("login.html")

@cont.route('/')
def contribute():
    if 'updater' in session and 'eventcode' in session and len(session['updater'])>=1 and len(session['eventcode'])>=1:
        updater=session['updater']
        eventcode=session['eventcode']
        title = "Please enter your contribution!"
        sites = get_sites()
        tls = get_tls()
        trash_items = get_trash_items()
        return render_template("contribution_input.html",
                               title=title,
                               sites=sites,
                               tls=tls,
                               trash_items=trash_items,
                               updater=updater,
                               eventcode=eventcode,
                               active_page='contribution')
    else:
        return render_template("login.html")


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
            print row
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

