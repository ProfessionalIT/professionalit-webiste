#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import template

provisorio_layout_path = template.render('templates/site', cache=False)

def provisorio():
    return provisorio_layout_path.layout()
