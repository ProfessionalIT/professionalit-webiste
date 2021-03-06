from web.template import CompiledTemplate, ForLoop, TemplateResult

_dummy = CompiledTemplate(lambda: None, 'dummy')
join_ = _dummy._join
escape_ = _dummy._escape

def layout_old():
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile.</title>\n'])
    extend_([u'    <meta name="language" content="pt-br"/>\n'])
    extend_([u'    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n'])
    extend_([u'    <meta name="copyright" content="Copyright (c) 2011 ProfessionalIT. This site\'s design and html code is licensed under the terms of the GPLv3 or (at your option) any later version.">\n'])
    extend_([u'    <meta name="organization name" content="ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile." />\n'])
    extend_([u'    <meta name="author" content="professionalit.com.br - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile."/>\n'])
    extend_([u'    <meta name="Description" content="Empresa de desenvolvimento de sistemas, sites, aplica\xe7\xf5es web e sistemas mobile." lang="pt-BR">\n'])
    extend_([u'    <meta name="Keywords" content="Sistema, Sites, WebSite, Mobile, Aplica\xe7\xf5es, Software, Desenvolvimento, Tecnologia, Open-Source, Python, Linux, Django, Web2Py, GAE, Google Apps" lang="pt-BR">\n'])
    extend_([u'    <meta name="rating" content="Sistemas, Sites, Aplica\xe7\xf5es Web, Aplica\xe7\xf5es Mobile">\n'])
    extend_([u'    <meta name="DC.title" content="professionalit.com.br">\n'])
    extend_([u'    <meta name="robots" content="ALL">\n'])
    extend_([u'    <meta name="googlebot" content="all" />\n'])
    extend_([u'    <meta name="generator" content="Geany 0.19" />\n'])
    extend_([u'    <meta name="classification" content="Internet" />\n'])
    extend_([u'    <meta name="distribution" content="Global" />\n'])
    extend_([u'    <meta name="revisit-after" content="2 weeks" />\n'])
    extend_([u"    <link rel='index' title='ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile.' href='http://www.professionalit.com.br' ></link>\n"])
    extend_([u'    <link rel="canonical" href="http://www.professionalit.com.br" ></link>\n'])
    extend_([u'    <link href="/static/css/style.css" rel="stylesheet" type="text/css"/>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'    <div id="main_panel">\n'])
    extend_([u'        <img src="/static/images/logotipo.png" alt="logotipo da ProfessionalIT." border="0"/>\n'])
    extend_([u'        <h1>Uma empresa de Solu\xe7\xf5es em Tecnologia.</h1>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="container">\n'])
    extend_([u'        <h3>No que somos especialistas e com certeza podemos te ajudar:</h3>\n'])
    extend_([u'        <ul id="nav">\n'])
    extend_([u'            <li id="selected"><a href="#">Sistemas</a></li>\n'])
    extend_([u'            <li><a href="#">Websites</a></li>\n'])
    extend_([u'            <li><a href="#">Aplica\xe7\xf5es Web</a></li>\n'])
    extend_([u'            <li><a href="#">Aplica\xe7\xf5es Mobile</a></li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="contact_panel" >\n'])
    extend_([u'         <p style="text-align:center;">Clientes, not\xedcias e acontecimentos em:</p>\n'])
    extend_([u'         <table>\n'])
    extend_([u'            <tr>\n'])
    extend_([u'                <td><a href="http://blog.professionalit.com.br" title="Blog da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."><img src="/static/images/Blogger_72.png" alt="Logotipo do Blogger." title="Blog da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."/></a></td>\n'])
    extend_([u'                <td><a href="http://www.twitter.com/professionalit" title="Twitter da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."><img src="/static/images/Twitter_72.png" alt="Logotipo do Twitter." title="Twitter da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile." /></a></td>\n'])
    extend_([u'                <td><a href="http://pt-br.facebook.com/pages/ProfessionalIT-Sistemas-Sites-Aplica%C3%A7%C3%B5es-Web-e-Aplica%C3%A7%C3%B5es-Mobile/172556429456889" title="Facebook da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."><img src="/static/images/Facebook_72.png" alt="Logotipo do Facebook." title="Facebook da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."/></a></td>\n'])
    extend_([u'            </tr>\n'])
    extend_([u'            <tr>\n'])
    extend_([u'                <td><a href="http://blog.professionalit.com.br" title="Blog da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile.">Nosso Blog</a></td>\n'])
    extend_([u'                <td><a href="http://www.twitter.com/professionalit" title="Twitter da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile.">Nosso Twitter</a></td>\n'])
    extend_([u'                <td><a href="http://pt-br.facebook.com/pages/ProfessionalIT-Sistemas-Sites-Aplica%C3%A7%C3%B5es-Web-e-Aplica%C3%A7%C3%B5es-Mobile/172556429456889" title="Facebook da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile.">Nosso Facebook</a></td>\n'])
    extend_([u'            </tr>\n'])
    extend_([u'         </table>\n'])
    extend_([u'         Estamos \xe0 tua disposi\xe7\xe3o: <span>+55 51 9390.3511</span> | E-mail: comercial@professionalit.com.br\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div style="width: 50%; margin: 0px auto;">\n'])
    extend_([u'        <h4>Deixe seu recado que entraremos em contato:</h4>\n'])
    extend_([u'        <form action="" method="post"> \n'])
    extend_([u'            <table> \n'])
    extend_([u'                <tr><th><label for="nome">Nome:</label></th><td><input name="nome" title="Informe o seu nome." maxlenght="250" type="text" id="nome" size="60"/></td></tr> \n'])
    extend_([u'                <tr><th><label for="email">E-mail:</label></th><td><input name="email" title="Informe o seu E-mail." maxlenght="250" type="text" id="email" size="60"/></td></tr> \n'])
    extend_([u'                <tr><th><label for="telefone">Telefone:</label></th><td><input name="telefone" title="Informe o seu telefone." maxlenght="250" type="text" id="telefone" size="60"/></td></tr> \n'])
    extend_([u'                <tr><th><label for="mensagem_adicional">Mensagem:</label></th><td><textarea title="Inclua sua mensagem." rows="15" id="mensagem_adicional" name="mensagem_adicional" cols="47"></textarea></td></tr> \n'])
    extend_([u'                <tr><th><label for="Submit!"></label></th><td><button type="submit" id="Submit!" name="Submit!">Enviar</button></td></tr> \n'])
    extend_([u'            </table> \n'])
    extend_([u'        </form> \n'])
    extend_([u'    </div>\n'])
    extend_([u'    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js" type="text/javascript"></script>\n'])
    extend_([u'    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/jquery-ui.min.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/javascript/jquery.spasticNav.js"></script>\n'])
    extend_([u'    <script type="text/javascript">\n'])
    extend_([u"        jQuery('#nav').spasticNav();\n"])
    extend_([u'    </script>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

layout_old = CompiledTemplate(layout_old, 'templates/site/layout_old.html')

def layout():
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile.</title>\n'])
    extend_([u'    <meta name="language" content="pt-br"/>\n'])
    extend_([u'    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n'])
    extend_([u'    <meta name="copyright" content="Copyright (c) 2012 ProfessionalIT. This site\'s design and html code is licensed under the terms of the GPLv3 or (at your option) any later version.">\n'])
    extend_([u'    <meta name="organization name" content="ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile." />\n'])
    extend_([u'    <meta name="author" content="professionalit.com.br - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile."/>\n'])
    extend_([u'    <meta name="Description" content="Empresa de desenvolvimento de sistemas, sites, aplica\xe7\xf5es web e sistemas mobile." lang="pt-BR">\n'])
    extend_([u'    <meta name="Keywords" content="Sistema, Sites, WebSite, Mobile, Aplica\xe7\xf5es, Software, Desenvolvimento, Tecnologia, Open-Source, Python, Linux, Django, Web2Py, GAE, Google Apps" lang="pt-BR">\n'])
    extend_([u'    <meta name="rating" content="Sistemas, Sites, Aplica\xe7\xf5es Web, Aplica\xe7\xf5es Mobile">\n'])
    extend_([u'    <meta name="DC.title" content="professionalit.com.br">\n'])
    extend_([u'    <meta name="robots" content="ALL">\n'])
    extend_([u'    <meta name="googlebot" content="all" />\n'])
    extend_([u'    <meta name="generator" content="Geany 0.19" />\n'])
    extend_([u'    <meta name="classification" content="Internet" />\n'])
    extend_([u'    <meta name="distribution" content="Global" />\n'])
    extend_([u'    <meta name="revisit-after" content="2 weeks" />\n'])
    extend_([u"    <link rel='index' title='ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile.' href='http://www.professionalit.com.br' ></link>\n"])
    extend_([u'    <link rel="canonical" href="http://www.professionalit.com.br" ></link>\n'])
    extend_([u'    <link href="/static/css/styles.css" rel="stylesheet" type="text/css"/>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'    <div id="main_panel" style="margin-bottom:80px;">\n'])
    extend_([u'        <img src="/static/images/novoLogo_black_invert.png" alt="logotipo da ProfessionalIT." border="0"/>\n'])
    extend_([u'        <h1>Uma empresa de Solu\xe7\xf5es em Tecnologia.</h1>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="container" style="margin-top:20px;">\n'])
    extend_([u'        <h3 style="margin-bottom: 30px">Onde com certeza podemos te ajudar:</h3>\n'])
    extend_([u'        <ul id="nav">\n'])
    extend_([u'            <li id="selected"><a href="#">SISTEMAS</a></li>\n'])
    extend_([u'            <li><a href="#">WEBSITES</a></li>\n'])
    extend_([u'            <li><a href="#">APLICA\xc7\xd5ES WEB</a></li>\n'])
    extend_([u'            <li><a href="#">APLICA\xc7\xd5ES MOBILE</a></li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="contact_panel" >\n'])
    extend_([u'         <p style="text-align:center;">Visite nossos canais:</p>\n'])
    extend_([u'         <table>\n'])
    extend_([u'            <tr>\n'])
    extend_([u'                <td><a href="http://blog.professionalit.com.br" title="Blog da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."><img src="/static/images/rss.png" alt="Logotipo do Blogger." title="Blog da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."/></a></td>\n'])
    extend_([u'                <td><a href="http://www.twitter.com/professionalit" title="Twitter da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."><img src="/static/images/twitter.png" alt="Logotipo do Twitter." title="Twitter da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile." /></a></td>\n'])
    extend_([u'                <td><a href="http://pt-br.facebook.com/pages/ProfessionalIT-Sistemas-Sites-Aplica%C3%A7%C3%B5es-Web-e-Aplica%C3%A7%C3%B5es-Mobile/172556429456889" title="Facebook da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."><img src="/static/images/facebook.png" alt="Logotipo do Facebook." title="Facebook da ProfessionalIT - Sistemas, Sites, Aplica\xe7\xf5es Web e Aplica\xe7\xf5es Mobile."/></a></td>\n'])
    extend_([u'            </tr>\n'])
    extend_([u'            <tr>\n'])
    extend_([u'                <td><a href="http://blog.professionalit.com.br">No Blog</a></td>\n'])
    extend_([u'                <td><a href="http://www.twitter.com/professionalit">No Twitter</a></td>\n'])
    extend_([u'                <td><a href="http://pt-br.facebook.com/pages/ProfessionalIT-Sistemas-Sites-Aplica%C3%A7%C3%B5es-Web-e-Aplica%C3%A7%C3%B5es-Mobile/172556429456889">No Facebook</a></td>\n'])
    extend_([u'            </tr>\n'])
    extend_([u'         </table>\n'])
    extend_([u'         <p style="text-align:center;margin-top:20px;margin-bottom:20px;">Interessado ?</p>\n'])
    extend_([u'         <p>Estamos \xe0 tua disposi\xe7\xe3o: <span>(51) 9390.3511</span> | E-mail: comercial@professionalit.com.br</p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="form_panel">\n'])
    extend_([u'        <h4>Ou deixe seu recado que entraremos em contato:</h4>\n'])
    extend_([u'        <fieldset style="width: 48%;margin:0px auto;border: none;">\n'])
    extend_([u'            <legend style="font-size: 28px;font-weight:bold;text-align:left;padding:05px;color:yellow;">Dados de Contato</legend>\n'])
    extend_([u'            <form action="" method="post">\n'])
    extend_([u'                <table> \n'])
    extend_([u'                    <tr><th><label for="nome">Nome:</label></th><td><input name="nome" title="Informe o seu nome." maxlenght="250" type="text" id="nome" size="60"/></td></tr> \n'])
    extend_([u'                    <tr><th><label for="email">E-mail:</label></th><td><input name="email" title="Informe o seu E-mail." maxlenght="250" type="text" id="email" size="60"/></td></tr> \n'])
    extend_([u'                    <tr><th><label for="telefone">Telefone:</label></th><td><input name="telefone" title="Informe o seu telefone." maxlenght="250" type="text" id="telefone" size="60"/></td></tr> \n'])
    extend_([u'                    <tr><th><label for="mensagem_adicional">Mensagem:</label></th><td><textarea title="Inclua sua mensagem." rows="15" id="mensagem_adicional" name="mensagem_adicional" cols="58"></textarea></td></tr> \n'])
    extend_([u'                    <tr><th><label for="Submit!"></label></th><td><button type="submit" id="Submit!" name="Submit!">Enviar</button></td></tr> \n'])
    extend_([u'                </table> \n'])
    extend_([u'            </form>\n'])
    extend_([u'        </fieldset>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="footer"><p>ProfessionalIT 2012 - Uma empresa do grupo <a href="#" title="MaxiG\xeanios - Genialidade em Solu\xe7\xf5es Tecnol\xf3gicas">MaxiG\xeanios - Genialidade em Solu\xe7\xf5es Tecnol\xf3gicas.</a></p></div>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

layout = CompiledTemplate(layout, 'templates/site/layout.html')

