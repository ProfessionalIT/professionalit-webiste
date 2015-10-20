# -*- coding: utf-8 -*-
import os
import web

import render_admin
import model
import forms

import logging

from paginator import Paginator, PaginatorSearch
from auth import requires_admin

urls = (
  "", "Main",
  "/", "Main",
  "/index", "Index",
  '/listar/(.*)', 'listar',
  '/inserir/(.*)', 'inserir',
  '/editar/(.*)/(.*)', 'editar',
  '/excluir/(.*)/(.*)', 'excluir'
)

class Main():
    @requires_admin
    def GET(self):
        raise web.seeother("/index")

class Index:
    @requires_admin
    def GET(self):
        return render_admin.index_admin()

class listar():
    @requires_admin
    def GET(self, param):
        entity = model.get_model_by_name(param)
        form = forms.getSearchForm(entity.exposed_search_properties())
        pagination = Paginator(web.input(), entity)
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        return render_admin.listar(form, pagination, display_message=display_message)

    @requires_admin
    def POST(self, param):
        """ Validate the search form to execute a search. """
        entity = model.get_model_by_name(param)
        form = forms.getSearchForm(entity.exposed_search_properties())
        if not form.validates():
            raise web.seeother('/listar/%s' % param)
        pagination = PaginatorSearch(web.input(), form, entity)
        display_message=''
        return render_admin.listar(form, pagination, display_message=display_message)

class inserir():
    @requires_admin
    def GET(self, param):
        frm = forms.getForm(param)
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        return render_admin.form(frm, titulo='Incluir %s' % param, verbo='incluir', display_message=display_message)

    @requires_admin
    def POST(self, param):
        frm = forms.getForm(param)
        if frm.validates():
            model.save_entity('%s' % param, frm.d)
            display_message='Inseriu o registro %s com sucesso !' % frm.d.titulo
            web.setcookie('display_message', display_message)
            if frm.d.operation == 'save':
                raise web.seeother('/inserir/%s' % param)
            else:
                raise web.seeother('/listar/%s' % param)
        else:
            return render_admin.form(frm, titulo='Incluir %s' % param, verbo='incluir', display_message='', estilo='table', )

class editar():
    @requires_admin
    def GET(self, param, record_id):
        entry = model.entity_by_id(model.get_model_by_name(param), record_id)
        frm = forms.getForm(param)
        frm.fill(entry)
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        return render_admin.form(frm, titulo='Alterar %s' % param, verbo='editar', display_message=display_message, estilo='table')

    @requires_admin
    def POST(self, param, record_id):
        frm = forms.getForm(param)
        if not frm.validates():
            return render_admin.form(frm, titulo='Alterar %s' % param, verbo='editar', estilo='table')
        display_message='Alterou o registro %s com sucesso !' % frm.d.titulo
        web.setcookie('display_message', display_message)
        if frm.d.operation == 'delete':
            raise web.seeother('/excluir/%(entity)s/%(id)s' % {'entity': param, 'id': record_id})
        elif frm.d.operation == 'save':
            model.save_entity('%s' % param, frm.d)
            raise web.seeother('/editar/%(entity)s/%(id)s' % {'entity': param, 'id': record_id})
        else:
            model.save_entity('%s' % param, frm.d)
            raise web.seeother('/listar/%s' % param)

class excluir():
    @requires_admin
    def GET(self, param, record_id):
        model.delete_entity(model.get_model_by_name(param), record_id)
        display_message='Excluiu o registro com sucesso !'
        web.setcookie('display_message', display_message)
        raise web.seeother('/listar/%s' % param)

app = web.application(urls, globals())

def main():
    pass
