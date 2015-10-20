# -*- coding: utf-8 -*-
import web
import render_website
from utils import break_string
from google.appengine.api import mail

urls = (
  '', 'Index',
  '/', 'Index',
  '/index', 'Index'
)

class Index:
    def GET(self):
        return render_website.provisorio()

    def POST(self):
        form = web.input()
        try:
            nome='O visitante ' + break_string(form.nome)
            telefone=' com o telefone: ' + break_string(form.telefone)
            email=' com o E-mail: ' + break_string(form.email)
            mensagem='Ele te deixou a seguinte mensagem: ' + '\n\t' + break_string(form.mensagem_adicional)
            mensagem_completa = nome + telefone + email + mensagem

            message = mail.EmailMessage()
            message.sender = 'lseverino@gmail.com'
            message.to = 'leandro@professionalit.com.br'
            message.subject = 'Contato realizado pelo Site'
            message.body = mensagem_completa
            message.send()
            return render_website.provisorio()
        except Exception:
            raise
        else:
            return render_website.provisorio()

app = web.application(urls, globals())

def main():
    pass
