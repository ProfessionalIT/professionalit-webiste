# -*- coding: utf-8 -*-
import model

def build_query(form):
    if form.valor != '':
        q = form.campo + form.criterio + "'" + form.valor + "'"
    elif form.campo == 'all':
        q = 'all'
    else:
        q = None
    return q

class Paginator:

    def __init__(self, params, classe, order=None):
        self.page = int(params.page if hasattr(params, 'page') else 0)
        self.pagesize = int(params.size if hasattr(params, 'size') else 10)
        self.query = params.q if hasattr(params, 'q') else None
        self.start = self.page if self.page == 0 else (self.page * self.pagesize)
        self.table_name = str(classe.get_list_title())
        self.classe_name=str(classe.get_class_name())
        self.icon_file='/static/images/%s.png' % self.classe_name
        self.exposed_attributes = classe.exposed_list_properties()
        self.order = order or classe.get_default_field_order()
        self.records = model.latest_records(classe, self.query, self.start, self.pagesize, self.order)
        self.total_records = model.count_records(classe)
        self.more_records = (len(self.records) >= self.pagesize) and (self.total_records > (self.pagesize + self.page))
        self.prev_page = None
        if self.page > 0:
            self.prev_page = str(self.page - 1)
        self.next_page = None
        if self.more_records:
            self.next_page = str(self.page + 1)
        self.records = self.records[:self.pagesize]
        self.record_counts = len(self.records)    

class PaginatorSearch:

    def __init__(self, params, form, classe, order=None):
        self.page = int(params.page if hasattr(params, 'page') else 0)
        self.pagesize = int(form.d.resultados or 10)
        self.query_ant = params.q if hasattr(params, 'q') else None
        self.start = self.page if self.page == 0 else (self.page * self.pagesize)
        self.table_name = str(classe.get_list_title())
        self.classe_name=str(classe.get_class_name())
        self.icon_file='/static/images/%s.png' % self.classe_name
        self.exposed_attributes = classe.exposed_list_properties()
        self.order = order or classe.get_default_field_order()
        self.query = build_query(form.d)
        if self.query_ant != 'None':
            if self.query is None:
                self.query = self.query_ant
        self.records = model.latest_records(classe, self.query, self.start, self.pagesize, self.order)
        self.total_records = model.count_records(classe)
        self.more_records = (len(self.records) >= self.pagesize) and (self.total_records > (self.pagesize + self.page))
        self.prev_page = None
        if self.page > 0:
            self.prev_page = str(self.page - 1)
        self.next_page = None   
        if self.more_records:   
            self.next_page = str(self.page + 1)
        self.records = self.records[:self.pagesize]  
        self.record_counts = len(self.records)
