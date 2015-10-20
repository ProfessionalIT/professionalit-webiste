#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import template

from auth import get_logged_user, get_logoff_url
from model import get_exposed_managed_tables 

import logging

admin_render_globals = {'user': get_logged_user(), 'logoff_url': get_logoff_url(), 'exposed_managed_tables': get_exposed_managed_tables()}
admin_template_path = template.render('templates/admin', cache=False, base="admin", globals=admin_render_globals)

def index_admin():
    return admin_template_path.index_admin()

def form(form, titulo=None, verbo=None, display_message=None, **kw):
    method = kw.pop('method', 'post')
    action = kw.pop('action', '')
    return admin_template_path.form(titulo, action, method, form, verbo, display_message)

def listar(frm, pagination, display_message=None):
    filtro = ''
    if pagination.query is not None and pagination.query != 'None' and pagination.query != 'all' and pagination.query !='':
        filtro = 'Filtrando por: %(query)s' % {'query': pagination.query}
    return admin_template_path.lista(frm, filtro, pagination, display_message)
