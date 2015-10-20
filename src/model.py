# -*- coding: utf-8 -*-
from google.appengine.api import users
from google.appengine.ext import db
import logging

from utils import slugify, versionate

from datetime import datetime

# Generic Functions
def get_exposed_managed_tables():
    values = []
    values.append({'model_table': 'Noticia', 'icon_file': '/static/images/Noticia.png', 'class_name': 'NOTÍCIAS'})
    values.append({'model_table': 'Evento', 'icon_file': '/static/images/Evento.png', 'class_name': 'EVENTOS'})
    values.append({'model_table': 'Revista', 'icon_file': '/static/images/Revista.png', 'class_name': 'REVISTAS'})
    values.append({'model_table': 'Grupo', 'icon_file': '/static/images/Grupo.png', 'class_name': 'GRUPOS'})
    values.append({'model_table': 'Aviso', 'icon_file': '/static/images/Aviso.png', 'class_name': 'AVISOS'})
    values.append({'model_table': 'Banner', 'icon_file': '/static/images/Banner.png', 'class_name': 'BANNERS'})
    values.append({'model_table': 'Foto', 'icon_file': '/static/images/Foto.png', 'class_name': 'FOTOS'})
    values.append({'model_table': 'Menu', 'icon_file': '/static/images/Menu.png', 'class_name': 'MENUS'})
    values.append({'model_table': 'Pagina', 'icon_file': '/static/images/Pagina.png', 'class_name': 'PÁGINAS'})
    return values

def latest_records(entity, q=None, start=1, PAGESIZE=10, order=None):
    limit=int(PAGESIZE)
    has_query=q != '' and q != 'NULL' and q != None and q != 'None' and q != 'all'
    if has_query:
        if order is not None:
            sql="SELECT * FROM %(entity)s WHERE %(query)s ORDER BY %(order)s" % {'entity': str(entity.kind()), 'query': q, 'order': order}
        else:
            sql="SELECT * FROM %(entity)s WHERE %(query)s" % {'entity': str(entity.kind()), 'query': q}
        query=db.GqlQuery(sql)
        return query.fetch(limit, start)
    else:
        if order is not None:
            try:
                query = db.Query(entity)
                query.order(order)
                return query.fetch(limit,int(start))
            except:
                query = db.Query(entity)
                query.order(order)
                return query.fetch(limit)
        else:
            try:
                return db.Query(entity).fetch(limit,int(start))
            except:
                return db.Query(entity).fetch(limit)

def count_records(entity):
    return entity.all().count()

def entity_by_id(entity, id):
    return entity.get_by_id(int(id))

def delete_entity(entity, id):
    entity=entity_by_id(entity, id)
    db.delete(entity)

def exists_entity(entity, field, value):
    q=db.Query(entity).filter('%s =' % field, value).get()
    return q

def find_slug(Entity, slug):
    q = db.Query(Entity).filter('slug =', slug).get()
    return q is not None

def get_model_by_name(name):
    if name == 'Noticia':
        return Noticia
    elif name == 'Evento':
        return Evento
    elif name == 'Revista':
        return Revista
    elif name == 'Grupo':
        return Grupo
    elif name == 'Aviso':
        return Aviso
    elif name == 'Banner':
        return Banner
    elif name == 'Foto':
        return Foto
    elif name == 'Parametro':
        return Parametro
    elif name == 'Pagina':
        return Pagina
    elif name == 'Menu':
        return Menu
    else:
        return None

def save_entity(entity, form):
    if entity == 'Noticia':
        save_noticia(form)
    elif entity == 'Evento':
        save_evento(form)
    elif entity == 'Revista':
        save_revista(form)
    elif entity == 'Grupo':
        save_grupo(form)
    elif entity == 'Aviso':
        save_aviso(form)
    elif entity == 'Banner':
        save_banner(form)
    elif entity == 'Foto':
        save_foto(form)
    elif entity == 'Parametro':
        save_parametro(form)
    elif entity == 'Pagina':
        save_pagina(form)
    elif entity == 'Menu':
        save_menu(form)
    else:
        pass

def get_entity_index_list(entity, filtro, valor, order, limit):
    query = db.Query(entity)
    if filtro is not None:
        q = db.Query(entity).filter('%s = ' % filtro, valor)
        q.order(order)
        return q.fetch(limit)
    else:
        query = db.Query(entity)
        query.order(order)
        return query.fetch(limit)

# App Models.
class Noticia(db.Model):
    titulo = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    data_hora = db.DateTimeProperty()
    author = db.UserProperty()
    palavras_chaves = db.StringProperty(required=True)
    intro_noticia = db.TextProperty(required=True)
    noticia_completa = db.TextProperty(required=True)
    thumb_noticia = db.StringProperty(required=False)
    foto_01 = db.StringProperty(required=False)
    thumb_01 = db.StringProperty(required=False)
    foto_02 = db.StringProperty(required=False)
    thumb_02 = db.StringProperty(required=False)
    foto_03 = db.StringProperty(required=False)
    thumb_03 = db.StringProperty(required=False)
    destaque = db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Noticia"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Notícias"

    @classmethod
    def get_default_field_order(cls):
        return "-data_hora"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo', 'Data/Hora', 'Destaque']
        fields = ['titulo', 'data_hora', 'destaque']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            if field == 'data_hora':
                data_hora = getattr(cls, field)
                if data_hora:
                    return data_hora.strftime('%d/%m/%Y %H:%M')
                else:
                    return None
            else:
                return getattr(cls, field)

def save_noticia(form):
    entity=exists_entity(Noticia, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_hora=datetime.strptime(form.data_hora,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.palavras_chaves=form.palavras_chaves
        entity.intro_noticia=form.intro_noticia
        entity.noticia_completa=form.noticia_completa
        entity.thumb_noticia=form.thumb_noticia
        entity.foto_01=form.foto_01
        entity.thumb_01=form.thumb_01
        entity.foto_02=form.foto_02
        entity.thumb_02=form.thumb_02
        entity.foto_03=form.foto_03
        entity.thumb_03=form.thumb_03
        entity.destaque=form.destaque
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_hora=datetime.strptime(form.data_hora,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.palavras_chaves=form.palavras_chaves
        entity.intro_noticia=form.intro_noticia
        entity.noticia_completa=form.noticia_completa
        entity.thumb_noticia=form.thumb_noticia
        entity.foto_01=form.foto_01
        entity.thumb_01=form.thumb_01
        entity.foto_02=form.foto_02
        entity.thumb_02=form.thumb_02
        entity.foto_03=form.foto_03
        entity.thumb_03=form.thumb_03
        entity.destaque=form.destaque
        db.put(entity)
    else:
        while find_slug(Noticia, slug):
            slug = versionate(slug)
        db.put(Noticia(
            titulo=form.titulo,
            slug=slug,
            data_hora = datetime.strptime(form.data_hora,'%Y-%m-%d %H:%M:%S'),
            author = users.get_current_user(),
            palavras_chaves=form.palavras_chaves,
            intro_noticia = form.intro_noticia,
            noticia_completa = form.noticia_completa,
            thumb_noticia = form.thumb_noticia,
            foto_01 = form.foto_01,
            thumb_01 = form.thumb_01,
            foto_02 = form.foto_02,
            thumb_02 = form.thumb_02,
            foto_03 = form.foto_03,
            thumb_03 = form.thumb_03,
            destaque=form.destaque))

def all_news_rss():
    query = db.Query(Noticia)
    query.order('-data_hora')
    result = query.fetch(1000)
    return result

class Evento(db.Model):
    titulo = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    data_publicacao = db.DateTimeProperty()
    data_hora_evento = db.DateTimeProperty()
    author = db.UserProperty()
    palavras_chaves = db.StringProperty(required=True)
    thumb_evento = db.StringProperty(required=False)
    foto_evento = db.StringProperty(required=False)
    texto = db.TextProperty(required=True)
    url_album_evento = db.StringProperty(required=False)
    url_canal_evento = db.StringProperty(required=False)
    destaque = db.StringProperty(required=False)

    @classmethod
    def get_class_name(cls):
        return "Evento"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Eventos"

    @classmethod
    def get_default_field_order(cls):
        return "-data_hora_evento"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('destaque', 'Destaque')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo', 'Data/Hora Evento', 'Publicado Em', 'Destaque']
        fields = ['titulo', 'data_hora_evento', 'data_publicacao', 'destaque']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            if field == 'data_hora_evento':
                data_hora_evento = getattr(cls, field)
                if data_hora_evento:
                    return data_hora_evento.strftime('%d/%m/%Y %H:%M')
                else:
                    return None
            elif field == 'data_publicacao':
                data_publicacao = getattr(cls, field)
                if data_publicacao:
                    return data_publicacao.strftime('%d/%m/%Y %H:%M')
                else:
                    return None
            else:
                return getattr(cls, field)

def save_evento(form):
    entity=exists_entity(Evento, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.data_hora_evento=datetime.strptime(form.data_hora_evento,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.palavras_chaves=form.palavras_chaves
        entity.thumb_evento=form.thumb_evento
        entity.foto_evento=form.foto_evento
        entity.texto=form.texto
        entity.url_album_evento=form.url_album_evento
        entity.url_canal_evento=form.url_canal_evento
        entity.destaque=form.destaque
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.data_hora_evento=datetime.strptime(form.data_hora_evento,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.palavras_chaves=form.palavras_chaves
        entity.thumb_evento=form.thumb_evento
        entity.foto_evento=form.foto_evento
        entity.texto=form.texto
        entity.url_album_evento=form.url_album_evento
        entity.url_canal_evento=form.url_canal_evento
        entity.destaque=form.destaque
        db.put(entity)
    else:
        while find_slug(Evento, slug):
            slug = versionate(slug)
        db.put(Evento(
            titulo=form.titulo,
            slug=slug,
            data_publicacao = datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'),
            data_hora_evento = datetime.strptime(form.data_hora_evento,'%Y-%m-%d %H:%M:%S'),
            author = users.get_current_user(),
            palavras_chaves=form.palavras_chaves,
            thumb_evento = form.thumb_evento,
            foto_evento = form.foto_evento,
            texto=form.texto,
            url_album_evento=form.url_album_evento,
            url_canal_evento=form.url_canal_evento,
            destaque=form.destaque))

def all_events():
    query = db.Query(Evento)
    result = query.fetch(1000)
    return result

def all_events_rss():
    query = db.Query(Evento)
    query.order('-data_publicacao')
    result = query.fetch(1000)
    return result

def nexts_eventos():
    hoje = datetime.now().date()
    query = db.Query(Evento)
    query.filter('data_hora_evento >=', hoje)
    query.order('-data_hora_evento')
    result = query.fetch(1000)
    return result

def next_eventos():
    from datetime import date, timedelta
    hoje = date.today()
    dia = timedelta(days=1)
    query = db.Query(Evento)
    query.filter('data_hora_evento >=', hoje-dia)
    query.filter('destaque = ', 'Sim')
    query.order('-data_hora_evento')
    result = query.fetch(1)
    return result

def ultimo_evento_publicado():
    import datetime
    last = db.Query(Evento).order('-data_publicacao').get()
    return last.data_publicacao if last else datetime.now()  

class Revista(db.Model):
    titulo = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    data_publicacao = db.DateTimeProperty()
    thumb_revista = db.StringProperty(required=True)
    link_arquivo = db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Revista"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Revistas"

    @classmethod
    def get_default_field_order(cls):
        return "-data_publicacao"
        
    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo', 'Publicado Em']
        fields = ['titulo', 'data_publicacao']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            if field == 'data_publicacao':
                data_publicacao = getattr(cls, field)
                if data_publicacao:
                    return data_publicacao.strftime('%d/%m/%Y %H:%M')
                else:
                    return None
            else:
                return getattr(cls, field)

def save_revista(form):
    entity=exists_entity(Revista, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.thumb_revista=form.thumb_revista
        entity.link_arquivo=form.link_arquivo
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.thumb_revista=form.thumb_revista
        entity.link_arquivo=form.link_arquivo
        db.put(entity)
    else:
        while find_slug(Revista, slug):
            slug = versionate(slug)
        db.put(Revista(
            titulo=form.titulo,
            slug=slug,
            data_publicacao = datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'),
            author = users.get_current_user(),
            thumb_revista = form.thumb_revista,
            link_arquivo = form.link_arquivo))

def latest_revista():
    query = db.Query(Revista)
    query.order('-data_publicacao')
    result = query.fetch(1)
    if result:
        return result[0]
    else:
        return None

class Grupo(db.Model):
    titulo = db.StringProperty(required=True)
    ordem = db.IntegerProperty(required=True)
    slug = db.StringProperty(required=True)
    thumb_banner = db.StringProperty(required=False)
    endereco_link = db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Grupo"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Grupos"

    @classmethod
    def get_default_field_order(cls):
        return "ordem"
        
    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo', 'Ordem']
        fields = ['titulo', 'ordem']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): return getattr(cls, field) 

def save_grupo(form):
    entity=exists_entity(Grupo, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.ordem=int(form.ordem)
        entity.slug=slug
        entity.thumb_banner=form.thumb_banner
        entity.endereco_link=form.endereco_link
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.ordem=int(form.ordem)
        entity.slug=slug
        entity.thumb_banner=form.thumb_banner
        entity.endereco_link=form.endereco_link
        db.put(entity)
    else:
        while find_slug(Grupo, slug):
            slug = versionate(slug)
        db.put(Grupo(
            titulo=form.titulo,
            ordem=int(form.ordem),
            slug=slug,
            thumb_banner = form.thumb_banner,
            endereco_link = form.endereco_link))

class Aviso(db.Model):
    titulo = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    data_publicacao = db.DateTimeProperty()
    author = db.UserProperty()
    texto = db.TextProperty(required=True)
    ativo = db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Aviso"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Avisos"

    @classmethod
    def get_default_field_order(cls):
        return "-data_publicacao"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo', 'Ativo', 'Publicado Em']
        fields = ['titulo', 'ativo', 'data_publicacao']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            if field == 'data_publicacao':
                data_publicacao = getattr(cls, field)
                if data_publicacao:
                    return data_publicacao.strftime('%d/%m/%Y %H:%M')
                else:
                    return None
            else:
                return getattr(cls, field)

def save_aviso(form):
    entity=exists_entity(Aviso, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.texto=form.texto
        entity.ativo=form.ativo
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.author=users.get_current_user()
        entity.texto=form.texto
        entity.ativo=form.ativo
        db.put(entity)
    else:
        while find_slug(Aviso, slug):
            slug = versionate(slug)
        db.put(Aviso(
            titulo=form.titulo,
            slug=slug,
            data_publicacao = datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'),
            author = users.get_current_user(),
            texto=form.texto,
            ativo=form.ativo))

class Banner(db.Model):
    titulo = db.StringProperty(required=True)
    ordem = db.IntegerProperty(required=True)
    slug = db.StringProperty(required=True)
    author = db.UserProperty()
    thumb_banner = db.StringProperty(required=True)
    foto_banner = db.StringProperty(required=True)
    endereco_site_patrocinador = db.StringProperty(required=False)
    exibir_pagina_inicial = db.StringProperty(required=True)
    status = db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Banner"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Banners"

    @classmethod
    def get_default_field_order(cls):
        return "titulo"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('exibir_pagina_inicial', 'Pág. Inicial'), ('status', 'Status')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo', 'Ordem', 'Exibir na Página Inicial', 'Status']
        fields = ['titulo', 'ordem', 'exibir_pagina_inicial', 'status']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): return getattr(cls, field) 

def save_banner(form):
    entity=exists_entity(Banner, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.ordem=int(form.ordem)
        entity.slug=slug
        entity.author=users.get_current_user()
        entity.thumb_banner=form.thumb_banner
        entity.foto_banner=form.foto_banner
        entity.endereco_site_patrocinador=form.endereco_site_patrocinador
        entity.exibir_pagina_inicial=form.exibir_pagina_inicial
        entity.status=form.status
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.ordem=int(form.ordem)
        entity.slug=slug
        entity.author=users.get_current_user()
        entity.thumb_banner=form.thumb_banner
        entity.foto_banner=form.foto_banner
        entity.endereco_site_patrocinador=form.endereco_site_patrocinador
        entity.exibir_pagina_inicial=form.exibir_pagina_inicial
        entity.status=form.status
        db.put(entity)
    else:
        while find_slug(Banner, slug):
            slug = versionate(slug)
        db.put(Banner(
            titulo=form.titulo,
            ordem=int(form.ordem),
            slug=slug,
            author = users.get_current_user(),
            thumb_banner = form.thumb_banner,
            foto_banner = form.foto_banner,
            endereco_site_patrocinador=form.endereco_site_patrocinador,
            exibir_pagina_inicial=form.exibir_pagina_inicial,
            status=form.status))

class Foto(db.Model):
    titulo = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    data_publicacao = db.DateTimeProperty()
    thumb = db.StringProperty(required=False)
    foto = db.StringProperty(required=False)
    status = db.StringProperty(required=True) #(sim, não)
    link_acao_foto = db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Foto"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Fotos"

    @classmethod
    def get_default_field_order(cls):
        return "titulo"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('status', 'Status')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo', 'Publicado Em', 'Status']
        fields = ['titulo', 'data_publicacao', 'status']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            if field == 'data_publicacao':
                data_publicacao = getattr(cls, field)
                if data_publicacao:
                    return data_publicacao.strftime('%d/%m/%Y %H:%M')
                else:
                    return None
            else:
                return getattr(cls, field)

def save_foto(form):
    entity=exists_entity(Foto, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.thumb=form.thumb
        entity.foto=form.foto
        entity.status=form.status
        entity.link_acao_foto=form.link_acao_foto
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.slug=slug
        entity.data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S')
        entity.thumb=form.thumb
        entity.foto=form.foto
        entity.status=form.status
        entity.link_acao_foto=form.link_acao_foto
        db.put(entity)
    else:
        while find_slug(Foto, slug):
            slug = versionate(slug)
        db.put(Foto(
            titulo=form.titulo,
            slug=slug,
            data_publicacao = datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'),
            thumb = form.thumb,
            foto = form.foto,
            status = form.status,
            link_acao_foto=form.link_acao_foto))

class Pagina(db.Model):
    titulo = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    descricao_completa = db.StringProperty(required=True)
    palavras_chaves = db.StringProperty(required=True)
    data_criacao = db.DateTimeProperty()
    ultima_alteracao = db.DateTimeProperty()
    usuario_alteracao = db.UserProperty()
    conteudo=db.TextProperty(required=False)
    
    @classmethod
    def get_class_name(cls):
        return "Pagina"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Páginas"

    @classmethod
    def get_default_field_order(cls):
        return "titulo"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo']
        fields = ['titulo']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): return getattr(cls, field) 

def save_pagina(form):
    entity=exists_entity(Pagina, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    if (entity is not None):
        entity.titulo=form.titulo
        entity.slug=slug
        entity.descricao_completa=form.descricao_completa
        entity.palavras_chaves=form.palavras_chaves
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.conteudo=form.conteudo
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.titulo=form.titulo
        entity.slug=slug
        entity.descricao_completa=form.descricao_completa
        entity.palavras_chaves=form.palavras_chaves
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.conteudo=form.conteudo
        db.put(entity)
    else:
        while find_slug(Pagina, slug):
            slug = versionate(slug)
        db.put(Pagina(
            titulo=form.titulo,
            slug=slug,
            descricao_completa=form.descricao_completa,
            palavras_chaves=form.palavras_chaves,
            data_criacao = datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'),
            ultima_alteracao = datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S'),
            usuario_alteracao = users.get_current_user(),
            conteudo=form.conteudo))

class Menu(db.Model):
    ordem = db.IntegerProperty(required=True)
    titulo = db.StringProperty(required=True)
    descricao = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    data_criacao = db.DateTimeProperty()
    ultima_alteracao = db.DateTimeProperty()
    usuario_alteracao = db.UserProperty()
    pagina=db.ReferenceProperty(Pagina, required=False, collection_name='pagina_set')
    endereco=db.StringProperty(required=False)
    menu_pai = db.SelfReferenceProperty(required=False)
    nivel =db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Menu"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Menus"

    @classmethod
    def get_default_field_order(cls):
        return "ordem"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('ordem', 'Ordem'), ('nivel', 'Nível'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Ordem', 'Nível', 'Titulo', 'Endereço']
        fields = ['ordem', 'nivel', 'titulo', 'endereco']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): return getattr(cls, field) 

def save_menu(form):
    entity=exists_entity(Menu, 'titulo', form.titulo)
    slug = slugify(form.titulo)
    parent = None
    if form.menu_pai is not None:
        parent = Menu.get_by_id(int(form.menu_pai))
    pagina = None
    if form.pagina is not None:
        pagina = Pagina.get_by_id(int(form.pagina))
        
    if (entity is not None):
        entity.ordem=int(form.ordem)
        entity.titulo=form.titulo
        entity.descricao=form.descricao
        entity.slug=slug
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.pagina=pagina
        entity.endereco=form.endereco        
        entity.menu_pai=parent
        entity.nivel=form.nivel
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.ordem=int(form.ordem)
        entity.titulo=form.titulo
        entity.descricao=form.descricao
        entity.slug=slug
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.pagina=pagina
        entity.endereco=form.endereco
        entity.menu_pai=parent
        entity.nivel=form.nivel
        db.put(entity)
    else:
        while find_slug(Menu, slug):
            slug = versionate(slug)
        db.put(Menu(
            ordem=int(form.ordem),
            titulo=form.titulo,
            descricao=form.descricao,
            slug=slug,
            data_criacao = datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'),
            ultima_alteracao = datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S'),
            usuario_alteracao = users.get_current_user(),
            pagina=pagina,
            endereco=form.endereco,
            menu_pai=parent,
            nivel=form.nivel))

def get_pagina(endereco):
    menu = db.Query(Menu).filter('endereco =', endereco).get()
    if menu != None:
        pagina = Pagina.get_by_id(int(menu.pagina.key().id()))
    else:
        slug = endereco.replace('/pagina/','')
        pagina = exists_entity(Pagina, 'slug', slug)
    return pagina or None

def get_avaliables_menus():
    sql="SELECT * FROM Menu WHERE ordem > 0 ORDER BY ordem, menu_pai, nivel"
    query=db.GqlQuery(sql)
    return query.fetch(10000)

def get_menu_itens():
    menus = get_avaliables_menus()
    menu_sup = 0
    tem_submenu = False
    menu_html = ''
    for menu in menus:
        nivel = int(menu.nivel)
        if nivel == 1:
            if tem_submenu:
                menu_html = menu_html + '</ul>'
                menu_html = menu_html + '</li>'
                tem_submenu = False
            menu_sup = str(menu.key().id())
            menu_html = menu_html + '<li class="first_level_menu"><a href="' + menu.endereco + '" class="menu" title="' + menu.descricao + '">' + menu.titulo + '</a>'
        elif nivel == 2:
            if menu.menu_pai is not None:
                if str(menu_sup) == str(menu.menu_pai.key().id()):
                    if tem_submenu == False:
                        tem_submenu = True
                        menu_html = menu_html + '<ul>'
                        menu_html = menu_html + '<li><a href="' + menu.endereco + '" title="' + menu.descricao + '">' + menu.titulo + '</a></li>'
                    else:
                        menu_html = menu_html + '<li><a href="' + menu.endereco + '" title="' + menu.descricao + '">' + menu.titulo + '</a></li>'
    if tem_submenu:
        menu_html = menu_html + '</ul>'
    menu_html = menu_html + '</li>'
    #logging.debug(' ======== HTML MENU ========= ' + menu_html)
    return menu_html
