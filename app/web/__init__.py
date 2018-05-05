#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
============================================================================
    FileName: __init__.py.py
    Desc:
    Author: zhoubangjun
    Date: 2018/5/4
=============================================================================
"""
from flask import Blueprint, render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@web.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
