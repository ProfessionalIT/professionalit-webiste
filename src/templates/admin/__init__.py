from web.template import CompiledTemplate, ForLoop, TemplateResult

_dummy = CompiledTemplate(lambda: None, 'dummy')
join_ = _dummy._join
escape_ = _dummy._escape

def form (titulo, action, method, form, verbo, display_message):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<h1>', escape_(titulo, True), u'</h1>\n'])
    extend_([u'<div class="painel_form">\n'])
    extend_([u'    <span class="show_message">', escape_(display_message, False), u'</span>\n'])
    extend_([u'    <h2><span class="titulo">Dados do Registro</span></h2>\n'])
    extend_([u'    <form action="', escape_(action, True), u'" method="', escape_(method, True), u'" name="operation_form" id="operation_form">\n'])
    extend_([u'        ', escape_(form.render(), False), u'\n'])
    extend_([u'        <span class="operations_field">Opera\xe7\xf5es:</span>\n'])
    if verbo == 'editar':
        extend_(['        ', u'<button type="submit" id="excluir_button" name="excluir_button" onclick="return setMode(\'delete\');">Excluir</button>\n'])
        extend_(['        ', u'<button type="submit" id="salvar_button" name="salvar_button" onclick="return setMode(\'save\');">Salvar</button>\n'])
    extend_([u'        <button type="submit" id="salvar_sair_button" name="salvar_sair_button" onclick="return setMode(\'save_exit\');">Salvar e Sair</button>\n'])
    extend_([u'    </form>\n'])
    extend_([u'</div>\n'])
    extend_([u'<script language="javascript" type="text/javascript">\n'])
    extend_([u'    function setMode(mode){\n'])
    extend_([u'        document.operation_form.operation.value=mode;\n'])
    extend_([u"        if (mode == 'delete'){ if (confirm('Deseja Realmente excluir o registro ?')) { return true; } else { return false; } } else { return true; }\n"])
    extend_([u'    }\n'])
    extend_([u'</script>\n'])
    extend_([u'\n'])

    return self

form = CompiledTemplate(form, 'templates/admin/form.html')

def admin (content):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-br">\n'])
    extend_([u'    <head>\n'])
    extend_([u'        <meta http-equiv="content-type" content="text/html; charset=utf-8"/>\n'])
    extend_([u'        <meta name="generator" content="Geany 0.18" />\n'])
    extend_([u'        <meta name="copyright" content="Copyright (c) 2010 ProfessionalIT. This site\'s design and html code is licensed under the terms of the GPLv3 or (at your option) any later version." />\n'])
    extend_([u'        <meta lang="pt-BR" name="Keywords" content="Ger\xeanciador, Admin, Manager." />\n'])
    extend_([u'        <meta lang="pt-BR" name="Description" content="M\xf3dulo Administrativo do Site." />\n'])
    extend_([u'        <meta name="robots" content="ALL"/>\n'])
    extend_([u'        <meta name="rating" content="General"/>\n'])
    extend_([u'        <meta name="author" content="Leandro Severino - ProfessionalIT"/>\n'])
    extend_([u'        <meta name="language" content="pt-br"/>\n'])
    extend_([u'        <meta name="DC.title" content="professionalit.com.br"/>\n'])
    extend_([u'        <meta name="revisit-after" content="1"/>\n'])
    extend_([u'        <link href="/static/images/alt.gif" rel="SHORTCUT ICON" />\n'])
    extend_([u'        <link href="/static/css/sge.css" type="text/css" rel="stylesheet" media="screen" />\n'])
    extend_([u'        <script src="/static/javascript/menu.js" type="text/javascript"></script>\n'])
    extend_([u'        <script src="/static/javascript/sge.js" type="text/javascript"></script>\n'])
    extend_([u'        <script src="/static/javascript/ajax.js" type="text/javascript"></script>\n'])
    extend_([u'        <!--JS da pagina-->\n'])
    extend_([u'        <!--[if lt IE 7.]>\n'])
    extend_([u'            <script defer type="text/javascript" src="/static/javascript/pngfix.js"></script>\n'])
    extend_([u'        <![endif]-->\n'])
    extend_([u'        <!-- tinyMCE -->\n'])
    extend_([u'        <script language="javascript" type="text/javascript" src="/static/javascript/tiny_mce/tiny_mce.js"></script>\n'])
    extend_([u'        <script language="javascript" type="text/javascript">\n'])
    extend_([u'            tinyMCE.init({\n'])
    extend_([u'                mode : "textareas",\n'])
    extend_([u'                theme : "advanced",\n'])
    extend_([u'                plugins : "safari,spellchecker,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,imagemanager,filemanager",\n'])
    extend_([u'                theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",\n'])
    extend_([u'                theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",\n'])
    extend_([u'                theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",\n'])
    extend_([u'                theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage",\n'])
    extend_([u'                theme_advanced_toolbar_location : "top",\n'])
    extend_([u'                theme_advanced_toolbar_align : "left",\n'])
    extend_([u'                theme_advanced_toolbar_statusbar_location : "bottom",\n'])
    extend_([u'                theme_advanced_resizing : true,\n'])
    extend_([u'            });\n'])
    extend_([u'        </script>\n'])
    extend_([u'        <!-- /tinyMCE -->\n'])
    extend_([u'        <!-- Calendar -->\n'])
    extend_([u'        <link href="/static/css/calendar.css" type="text/css" rel="stylesheet" media="screen" />\n'])
    extend_([u'        <script src="/static/javascript/jquery.js" type="text/javascript"></script>\n'])
    extend_([u'        <script src="/static/javascript/calendar.js" type="text/javascript"></script>\n'])
    extend_([u'        <script type="text/javascript">\n'])
    extend_([u'        <!--\n'])
    extend_([u'            function calendar_init() {\n'])
    extend_([u'              try { jQuery("input.datetime").focus( function() {Calendar.setup({\n'])
    extend_([u'                 inputField:this.id, ifFormat:"%Y-%m-%d %H:%M:%S", showsTime: true,timeFormat: "24"\n'])
    extend_([u'              }); }); } catch(e) {};\n'])
    extend_([u'            };\n'])
    extend_([u'        //-->\n'])
    extend_([u'        </script>\n'])
    extend_([u'        <!-- /Calendar -->\n'])
    extend_([u'        <title>M\xf3dulo Administrativo - Lind\xf3ia T\xeanis Clube - Vers\xe3o beta 001a.</title>\n'])
    extend_([u'    </head>\n'])
    extend_([u'    <body>\n'])
    extend_([u'        <!-- Menu bar. -->\n'])
    extend_([u'        <DIV class="menuBar">\n'])
    for item in loop.setup(exposed_managed_tables):
        extend_(['            ', u'<A class="menuButton" href="/admin/listar/', escape_(item['model_table'], False), u'" title="', escape_(item['class_name'], False), u'"><img src="', escape_(item['icon_file'], False), u'" class="icon_menu" alt="', escape_(item['class_name'], False), u'" title="', escape_(item['class_name'], False), u'" />', escape_(item['class_name'], False), u'</A>\n'])
    extend_([u'        </DIV>\n'])
    extend_([u'        <div id="innerContent">\n'])
    extend_([u'            ', escape_(content, False), u'\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div id="copyrightMessage">\n'])
    extend_([u'            <p>\n'])
    extend_([u'                <SPAN><A href="http://www.professionalit.com.br" title="ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile.">ProfessionalIT 2010</A></SPAN><SPAN>| +55 51 3032.3043</SPAN><SPAN>| comercial@professionalit.com.br</SPAN> |<SPAN>Usu\xe1rio: <strong class="user_destaq">', escape_(user, True), u'</strong> | <A href="', escape_(logoff_url, True), u'" title="Efetuar o Log-Off no sistema.">Log-Off.</A></SPAN><SPAN>| <a href="/admin/index" title="P\xe1gina Inicial.">Home</a>.</SPAN>\n'])
    extend_([u'            </p>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <script type="text/javascript">\n'])
    extend_([u'        <!--\n'])
    extend_([u'            jQuery(document).ready(function(){calendar_init();});\n'])
    extend_([u'        //-->\n'])
    extend_([u'        </script>\n'])
    extend_([u'    </body>\n'])
    extend_([u'</html>\n'])

    return self

admin = CompiledTemplate(admin, 'templates/admin/admin.html')

def lista (form, filtro, pagination, display_message):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<h2 class="form_title"><img src="', escape_(pagination.icon_file, True), u'" class="icon_menu" alt="', escape_(pagination.table_name, True), u'" title="', escape_(pagination.table_name, True), u'" />', escape_(pagination.table_name, True), u'</h2>\n'])
    extend_([u'<form name="pesquisa" action="/admin/listar/', escape_(pagination.classe_name, True), u'" method="POST">\n'])
    extend_([u'    <fieldset>\n'])
    extend_([u'        <legend class="alignLeft">Filtro de Registros:</legend>\n'])
    extend_([u'        ', escape_(form.render_css(), False), u'\n'])
    extend_([u'    </fieldset>\n'])
    extend_([u'</form>\n'])
    extend_([u'<div class="painel">\n'])
    extend_([u'    <span class="show_message">', escape_(display_message, False), u'</span>\n'])
    if filtro:
        extend_(['    ', u'<h2 class="margin05px"><span class="titulo">Listagem de Registros</span><span class="filtro">', escape_(filtro, True), u'</span></h2>\n'])
    else:
        extend_(['    ', u'<h2 class="margin05px"><span class="titulo">Listagem de Registros</span></h2>\n'])
    extend_([u'    <p id="painel_new_record"><span class="button"><a href="/admin/inserir/', escape_(pagination.classe_name, True), u'" title="Incluir novo registro.">Incluir Registo</a></span></p>\n'])
    extend_([u'    <table cellspacing="0" cellpadding="0" id="list">\n'])
    extend_([u'        <thead>\n'])
    extend_([u'            <tr>\n'])
    extend_([u'                <th>C\xf3digo</th>\n'])
    for colunm in loop.setup(pagination.exposed_attributes['colunms']):
        extend_(['                ', u'<th>', escape_(colunm, True), u'</th>\n'])
    extend_([u'            </tr>\n'])
    extend_([u'        </thead>\n'])
    extend_([u'        <tbody>\n'])
    for record in loop.setup(pagination.records):
        extend_(['            ', u'<tr>\n'])
        extend_(['            ', u'    <td><a href="/admin/editar/', escape_(pagination.classe_name, True), u'/', escape_(record.key().id(), True), u'" title="Editar o Registro.">', escape_(record.key().id(), True), u'</a></td>\n'])
        for field in loop.setup(pagination.exposed_attributes['fields']):
            extend_(['                ', u'<td>', escape_(record.get_field_value(field), False), u'</td>\n'])
        extend_(['            ', u'</tr>\n'])
    extend_([u'        </tbody>\n'])
    extend_([u'    </table>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="panel_records">\n'])
    if pagination.prev_page:
        extend_([u'<a href="/admin/listar/', escape_(pagination.classe_name, True), u'?page=', escape_(pagination.prev_page, True), u'&size=', escape_(pagination.pagesize, True), u'&q=', escape_(pagination.query, True), u'" title="P\xe1gina Anterior."><img src="/static/images/back.png" alt="P\xe1gina Anterior." title="P\xe1gina Anterior." /></a>\n'])
        extend_([u'\n'])
    if not pagination.prev_page and not pagination.next_page and pagination.total_records > 0:
        extend_([u'<span>Mostrando de 1 \xe0 ', escape_(pagination.record_counts, True), u' registros.</span>\n'])
    elif pagination.total_records == 0:
        extend_([u'<span>Sem Registros.</span>\n'])
    else:
        if (int(pagination.pagesize) + int(pagination.start)) > int(pagination.total_records):
            extend_([u'<span>Mostrando registros de ', escape_((int(pagination.start) + 1), True), u' \xe0 ', escape_((int(pagination.total_records)), True), u'.</span>\n'])
        else:
            extend_([u'<span>Mostrando registros de ', escape_((int(pagination.start) + 1), True), u' \xe0 ', escape_((int(pagination.pagesize) + int(pagination.start)), True), u' no total de ', escape_(pagination.total_records, True), u' registros.</span>\n'])
            extend_([u'\n'])
    if pagination.next_page:
        extend_([u'<a href="/admin/listar/', escape_(pagination.classe_name, True), u'?page=', escape_(pagination.next_page, True), u'&size=', escape_(pagination.pagesize, True), u'&q=', escape_(pagination.query, True), u'" title="Pr\xf3xima P\xe1gina."><img src="/static/images/forward.png" alt="Pr\xf3xima P\xe1gina." title="Pr\xf3xima P\xe1gina." /></a>\n'])
    extend_([u'</div>\n'])

    return self

lista = CompiledTemplate(lista, 'templates/admin/lista.html')

def index_admin():
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<DIV id="innerWindow" align="center">\n'])
    extend_([u'    <img src="/static/images/novoLogotipo.png" alt="Imagem de Background." title="Imagem de Background." align="center" class="img_main_page" />\n'])
    extend_([u'</DIV>\n'])

    return self

index_admin = CompiledTemplate(index_admin, 'templates/admin/index_admin.html')

