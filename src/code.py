# -*- coding: utf-8 -*-
import web

import website
import manager

urls = (
  '/admin', manager.app,
  '', website.app
)

class Main():
    def GET(self):
        raise web.seeother("/index")

#web.config.debug = False
app = web.application(urls, globals())
app = app.gaerun()
