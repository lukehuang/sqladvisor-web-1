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
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True,
                static_folder='../static',
                template_folder='../templates')

    app.config.from_object('config')
    # 加载定义在instance文件夹中的配置文件
    app.config.from_pyfile('config.py')
    register_blueprint(app)

    return app


def register_blueprint(app):
    from web.sqladvisor import web
    app.register_blueprint(web)

