#!/usr/bin/python

"""
Budget chart
by Dmitry Shvetsov (@shvetsovdm)

External dependencies: lxml, pygal

For using create budget.ini file in same
directory where current script is.
    
Example:

    [DEFAULT]
    labels=Jan,Feb,Mar
    guaranteed_income=12000,12000,18000
    guaranteed_expense=10000,10000,10000
    additional_expense=0,0,9000

"""

import pygal
import configparser

config = configparser.ConfigParser()
config.read('budget.ini')
default_config = config['DEFAULT']

if default_config:

    line_chart = pygal.Line()

    line_chart.title = 'Budget Chart'

    line_chart.x_labels = default_config['labels'].split(',')

    # guaranteed income
    g_income = [float(elem) for elem in default_config['guaranteed_income'].split(',')]
    # guaranteed expense
    g_expense = [float(elem) for elem in default_config['guaranteed_expense'].split(',')]
    # additional expense
    a_expense = [float(elem) for elem in default_config['additional_expense'].split(',')]

    balance = [ginc + gexp + aexp for ginc, gexp, aexp in zip(g_income, g_expense, a_expense)]
    cum_balance = [value + sum(balance[:index]) for index, value in enumerate(balance)]

    line_chart.add('Guaranteed Income', g_income, stroke_style = {'width': 2, 'dasharray': '3, 6, 12, 24'})
    line_chart.add('Guaranteed Expense', g_expense, stroke_style = {'width': 2, 'dasharray': '3, 6, 12, 24'})
    line_chart.add('Additional Expense', a_expense, stroke_style = {'width': 2, 'dasharray': '3, 6, 12, 24'})
    line_chart.add('Balance', balance, stroke_style = {'width': 2})
    line_chart.add('Cum Balance', cum_balance, fill = True, stroke_style = {'width': 2})

    line_chart.render_in_browser()
