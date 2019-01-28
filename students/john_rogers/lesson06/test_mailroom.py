#!/usr/bin/env python3
"""
test_mailroom.py: use pytest to validate functions in mailroom.py
Author: JohnR
Version: 0.8
Last updated: 1/24/2019
Notes:
"""

import pytest
import os
from datetime import date


from mailroom_L6 import thank_all
from mailroom_L6 import exit_menu
from mailroom_L6 import save_report
from mailroom_L6 import form_letter
from mailroom_L6 import sorted_list
from mailroom_L6 import print_summary


@pytest.fixture
def data():
    db = {'sting': [13.45, 214.34, 123.45, 1433.23, 1243.13],
          'bono': [7843.34, 35.55, 732.34],
          'oprah': [66.34, 32.23, 632.21, 66.67],
          'yoko': [34.34, 4.34],
          'santa': [5334.00, 254.34, 64324.23, 2345.23, 5342.24],
          }
    return db


@pytest.mark.parametrize('name, amount', [
    ('bill', 100.01),
    ('mark', 24100),
    ('sammy', 2345100.51),
    ('sarah', 00.01),
    ('zoe', 150.99),
])
def test_form_letter(name, amount):
    today = date.today()
    letter = f'Hey {name.capitalize()}, thanks for your' \
             f' donations! As of today, {today},' \
             f' you have donated a total of ${amount}.'
    assert form_letter(name, amount) == letter


def test_exit_menu(data):
    with pytest.raises(SystemExit):
        exit_menu(data)


def test_save_report(data):
    today = date.today()
    save_report(data)
    assert os.path.isfile(f'sting.{today}.txt')
    assert os.path.isfile(f'bono.{today}.txt')
    assert os.path.isfile(f'oprah.{today}.txt')
    assert os.path.isfile(f'yoko.{today}.txt')
    assert os.path.isfile(f'santa.{today}.txt')


def test_sorted_list(data):
    my_list = [[['santa'], [77600.04], [5], [15520.01]],
                 [['bono'], [8611.23], [3], [2870.41]],
                 [['sting'], [3027.6], [5], [605.52]],
                 [['oprah'], [797.45], [4], [199.36]],
                 [['yoko'], [38.68], [2], [19.34]]]
    assert sorted_list(data) == my_list


# TODO: Test these beyond just returning None
def test_print_summary(data):
    assert print_summary(data) is None


def test_thank_all(data):
    assert thank_all(data) is None


