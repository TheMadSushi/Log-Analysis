#!/usr/bin/env python
# LOG ANALYSIS PROJECT

import psycopg2  # Imports DB API for postgresql

""" This module provides analysis of log data about authors
and articles accessed from a website from database using postgresql"""

# Queries to be run to get the required result
query1 = "SELECT * FROM popular_article_vew"
query2 = "SELECT * FROM popular_author_vew"
query3 = "SELECT * FROM err_log_vew"


def popular_articles(query1):
    """Method printing three most popular articles"""

    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute(query1)
    results = cur.fetchall()
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("%s--%d" % (title, views))
    db.close()


def popular_authors(query2):
    """"Method printing popular author of all time"""

    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute(query2)
    results = cur.fetchall()
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        print("%s--%d" % (name, views))
    db.close()


def error_percent(query3):
    """"Method that prints a day when more than 1% requests lead to error"""

    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute(query3)
    results = cur.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        err_prc = results[i][1]
        print("%s--%.1f %%" % (date, err_prc))
    db.close()


if __name__ == "__main__":
    """Main method"""

    print("THREE MOST POPULAR ARTICLES ARE:")
    popular_articles(query1)
    print("\n")
    print("MOST POPULAR AUTHORS OF ALL TIME ARE:")
    popular_authors(query2)
    print("\n")
    print("DAY WHEN MORE THAN 1% REQUESTS LED TO ERROR")
    error_percent(query3)
