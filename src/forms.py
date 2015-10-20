#!/usr/bin/python
# -*- coding: utf-8 -*-
import gae_form as form
import model

# Commons Validators Expressions
vemail = form.regexp("^([0-9a-zA-Z]+([_.-]?[0-9a-zA-Z]+)*@[0-9a-zA-Z]+[0-9,a-z,A-Z,.,-]*(.){1}[a-zA-Z]{2,4})+$", "Precisa ser um endereco de e-mail válido !.")
vdigito = form.regexp("\d+", "Precisa ser um digito")
vmoeda = form.regexp("^\d{1,5}(\.\d{1,2})?$", "Precisa ser um valor inteiro OU com duas casas decimais !")
vdata =  form.regexp("^(((0[1-9]|[12][0-9]|3[01])([/])(0[13578]|10|12)([/])(\d{4}))|(([0][1-9]|[12][0-9]|30)([/])(0[469]|11)([/])(\d{4}))|((0[1-9]|1[0-9]|2[0-8])([/])(02)([/])(\d{4}))|((29)(\.|-|\/)(02)([/])([02468][048]00))|((29)([/])(02)([/])([13579][26]00))|((29)([/])(02)([/])([0-9][0-9][0][48]))|((29)([/])(02)([/])([0-9][0-9][2468][048]))|((29)([/])(02)([/])([0-9][0-9][13579][26])))$", "Precisa ser uma data no formato dd/mm/yyyy !")
vdatafull =  form.regexp("^\d{4}-([\d]|0[0-9]|1[0,1,2])-([0-9]|[0,1,2][0-9]|3[0,1]) ([0-1][0-9]|[2][0-3])(:([0-5][0-9])){1,2}(:([0-5][0-9])){1,2}$", "Precisa ser uma data e hora no formato yyyy-mm-dd hh:mm:ss !")
vurl = form.regexp("^(http[s]?://|ftp://)?(www\.)?[a-zA-Z0-9-\.]+\.(com|org|net|mil|edu|ca|co.uk|com.au|gov|br)$", "Precisa ser um endereço Web Válido !.")
vtelefone = form.regexp("^\(?\d{2}\)?[\s-]?\d{4}-?\d{4}$", "Precisa ser um telefone no formato (99) 9999-9999")
vcep = form.regexp("^[0-9]{2}\.[0-9]{3}-[0-9]{3}$", "Precisa estar no formato 99.999-999 !")
vcnpj = form.regexp("\d{2,3}.\d{3}.\d{3}/\d{4}-\d{2}", "Precisa estar no formato 99.999.999/9999-99 !")

# App Forms
def getSearchForm(fields):
    search_form = form.GAEForm(
            form.Dropdown('campo', fields, description='Campo:', onblur='clean_search(this.value, valor);', onclick='clean_search(this.value, valor);' ),
            form.Dropdown('criterio', [('=', '='), ('!=', '!='), ('IN', 'IN'), ('<', '<'), ('<=', '<='), ('>=', '>='), ('>', '>')], description='Critério:'),
            form.Textbox('valor', size=20, description="Valor:"),
            form.Button('Pesquisa', html="Pesquisar", type="submit"),
            form.Dropdown('resultados', [('10', '10'), ('50', '50'), ('100', '100')], onchange='form.submit()',description='Qtde Registros:'),
    )
    return search_form

def getForm(param):
    if param == 'Noticia':
        return getNoticiaForm()
    elif param == 'Evento':
        return getEventoForm()
    elif param == 'Revista':
        return getRevistaForm()
    elif param == 'Grupo':
        return getGrupoForm()
    elif param == 'Aviso':
        return getAvisoForm()
    elif param == 'Banner':
        return getBannerForm()
    elif param == 'Foto':
        return getFotoForm()
    elif param == 'Parametro':
        return getParametroForm()
    elif param == 'Pagina':
        return getPaginaForm()
    elif param == 'Menu':
        return getMenuForm()
    else:
        return None

def getNoticiaForm():
    noticia_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Notícia.", description='Titulo:'),
        form.Textbox('data_hora', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de publicação da Notícia.", readonly="readonly", description='Data e Hora: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlenght="250", title="Palavras Chaves da Notícia separadas por vírgula.", description='Palavras Chaves:'),
        form.Textarea('intro_noticia', form.notnull, cols="70", rows="20", title="Texto Introdutório da Notícia.", description='Introdução da Notícia:'),
        form.Textarea('noticia_completa', form.notnull, cols="70", rows="20", title="Texto Completo da Notícia.", description='Notícia Completa:'),
        form.Textbox('thumb_noticia', size="60", maxlenght="250", title="URL/Endereço da foto miniatura da Notícia.", description='URL Miniatura:'),
        form.Textbox('foto_01', size="60", maxlenght="250", title="URL/Endereço da Foto 01 da  Notícia.", description='URL Foto 01:'),
        form.Textbox('thumb_01', size="60", maxlenght="250", title="URL/Endereço da foto miniatura 01 da Notícia.", description='URL Miniatura Foto 01:'),
        form.Textbox('foto_02', size="60", maxlenght="250", title="URL/Endereço da Foto 02 da  Notícia.", description='URL Foto 02:'),
        form.Textbox('thumb_02', size="60", maxlenght="250", title="URL/Endereço da foto miniatura 02 da Notícia.", description='URL Miniatura Foto 02:'),
        form.Textbox('foto_03', size="60", maxlenght="250", title="URL/Endereço da Foto 03 da  Notícia.", description='URL Foto 03'),
        form.Textbox('thumb_03', size="60", maxlenght="250", title="URL/Endereço da foto miniatura 03 da Notícia.", description='URL Miniatura Foto 03:'),
        form.Dropdown('destaque', [('Sim', 'Sim'), ('Nao', 'Nao')], title="A Notícia deve ser exibida na página inicial do site ?", description='Notícia é Destaque ?:')
    )
    return noticia_form

def getEventoForm():
    evento_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome do Evento.", description='Titulo:'),
        form.Textbox('data_publicacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de publicação do Evento.", readonly="readonly", description='Publicado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('data_hora_evento', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora do Evento.", readonly="readonly", description='Data e Hora: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlenght="250", title="Palavras Chaves do Evento separadas por vírgula.", description='Palavras Chaves:'),
        form.Textbox('thumb_evento', size="60", maxlenght="250", title="URL/Endereço da miniatura da foto do Evento.", description='URL Miniatura:'),
        form.Textbox('foto_evento', size="60", maxlenght="250", title="URL/Endereço da foto do Evento.", description='URL Banner:'),
        form.Textarea('texto', form.notnull, cols="70", rows="25", title="Texto completo descritivo do Evento.", description='Descrição do Evento:'),
        form.Textbox('url_album_evento', size="60", maxlenght="250", title="URL/Endereço do Albúm de Fotos do Evento.", description='Albúm de Fotos do Evento:'),
        form.Textbox('url_canal_evento', size="60", maxlenght="250", title="URL/Endereço do Canal de Vídeos do Evento.", description='Canal de Vídeo do Evento:'),
        form.Dropdown('destaque', [('Sim', 'Sim'), ('Nao', 'Nao')], title="O Evento deve ser exibida na página inicial do site ?", description='Evento é Destaque ?:', value='Nao')
    )
    return evento_form

def getRevistaForm():
    revista_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Revista.", description='Titulo:'),
        form.Textbox('data_publicacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de publicação da Revista.", readonly="readonly", description='Publicado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('thumb_revista', form.notnull, size="60", maxlenght="250", title="URL/Endereço da miniatura da foto da Revista.", description='URL Miniatura:'),
        form.Textbox('link_arquivo', form.notnull, size="60", maxlenght="250", title="Link para o arquivo PDF da Revista.", description='Link para o Arquivo PDF:')
    )
    return revista_form

def getGrupoForm():
    grupo_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome do Grupo.", description='Titulo:'),
        form.Textbox('ordem', vdigito, size="10", maxlenght="50", title="Ordem de Exibição do Menu na Página. Deve seguir a sequência para que o menu funcione.", description='Ordem de Exibição:'),
        form.Textbox('thumb_banner', form.notnull,  size="60", maxlenght="250", title="URL/Endereço do Banner do Grupo.", description='URL Banner:'),
        form.Textbox('endereco_link', form.notnull, size="60", maxlenght="250", title="URL/Endereço do link a ser acionado ao se clicar no banner do Grupo.", description='Link no Banner:')
    )
    return grupo_form

def getAvisoForm():
    aviso_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome do Aviso.", description='Titulo:'),
        form.Textbox('data_publicacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de publicação do Aviso.", readonly="readonly", description='Publicado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textarea('texto', form.notnull, cols="70", rows="25", title="Texto do Aviso.", description='Texto do Aviso:'),
        form.Dropdown('ativo', [('Sim', 'Sim'), ('Nao', 'Nao')], title="O Aviso está ativo ?", description='Aviso ativo ?:')
    )
    return aviso_form

def getBannerForm():
    banner_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome do Banner.", description='Titulo:'),
        form.Textbox('ordem', vdigito, size="10", maxlenght="50", title="Ordem de Exibição do Menu na Página. Deve seguir a sequência para que o menu funcione.", description='Ordem de Exibição:'),
        form.Textbox('thumb_banner',  size="60", maxlenght="250", title="URL/Endereço da miniatura da foto do Banner.", description='URL Miniatura:'),
        form.Textbox('foto_banner', form.notnull, size="60", maxlenght="250", title="URL/Endereço da imagem/foto do Banner.", description='URL Banner:'),
        form.Textbox('endereco_site_patrocinador', size="60", maxlenght="250", title="URL/Endereço do link que deve ser acionado ao se clicar do Banner.", description='Link no Banner:'),
        form.Dropdown('exibir_pagina_inicial', [('Sim', 'Sim'), ('Nao', 'Nao')], title="Banner deve ser exibido na página inicial do site ?", description='Exibe na Página Inicial ?:'),
        form.Dropdown('status', [('Ativo', 'Ativo'), ('Inativo', 'Inativo')], title="Banner Ativo ?", description='Banner Ativo ?:')
    )
    return banner_form

def getFotoForm():
    foto_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Foto.", description='Titulo:'),
        form.Textbox('data_publicacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de publicação da Foto.", readonly="readonly", description='Publicado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('thumb', form.notnull, size="60", maxlenght="250", title="URL/Endereço da miniatura da Foto.", description='URL Miniatura:'),
        form.Textbox('foto', form.notnull, size="60", maxlenght="250", title="URL/Endereço da Foto.", description='URL Foto:'),
        form.Dropdown('status', [('Ativo', 'Ativo'), ('Inativo', 'Inativo')], title="Foto Ativa ?", description='Foto Ativa ?:'),
        form.Textbox('link_acao_foto', form.notnull, size="60", maxlenght="250", title="Link que deve ser acionado ao se clicar na Foto.", description='Link de Ação da Foto:')
    )
    return foto_form

def getPaginaForm():
    pagina_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Página.", description='Titulo:'),
        form.Textbox('slug', size="60", maxlenght="250", title="URL da Página.", readonly="readonly", description='URL da Página'),
        form.Textbox('descricao_completa', form.notnull, size="60", maxlenght="250", title="Descrição Completa da Página.", description='Descrição Completa:'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlenght="250", title="Palavras Chaves da Página separadas por vírgula.", description='Palavras Chaves:'),
        form.Textbox('data_criacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de criação da Página.", readonly="readonly", description='Criado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('ultima_alteracao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de última atualização da Página.", readonly="readonly", description='Última Alteração em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textarea('conteudo', form.notnull, cols="70", rows="25", title="Conteúdo da Página.", description='Conteúdo da Página:')
    )
    return pagina_form

def getMenuForm():
    menu_list = model.Menu.all()
    menu_options = [(str(row.key().id()), row.titulo) for row in menu_list]
    pagina_list = model.Pagina.all()
    pagina_options = [(str(row.key().id()), row.titulo) for row in pagina_list]
    menu_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('ordem', vdigito, size="10", maxlenght="50", title="Ordem de Exibição do Menu na Página. Deve seguir a sequência para que o menu funcione.", description='Ordem de Exibição:'),
        form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Página.", description='Titulo:'),
        form.Textbox('descricao', form.notnull, size="60", maxlenght="250", title="Descrição do Menu.", description='Descrição:'),
        form.Textbox('data_criacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de criação da Página.", readonly="readonly", description='Criado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('ultima_alteracao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de última atualização da Página.", readonly="readonly", description='Última Alteração em: (YYYY-MM-DD HH:MM:SS)'),
        form.Dropdown('pagina', pagina_options, title="Página que deve ser exibida ao clicar no menu.", description='Página: '),
        form.Textbox('endereco', form.notnull, size="60", maxlenght="250", title="Endereço do link.", description='Endereço do Link:'),
        form.Dropdown('menu_pai', menu_options, title="Menu Pai/Superior do Menu.", description='Menu Superior: '),
        form.Dropdown('nivel', [('0', '0'), ('1', '1'), ('2', '2')], title="Nível do Menu: 0 - MenuBar, 1-Menu Principal, 2-Menu Interno.", description='Nível: ')
    )
    return menu_form
