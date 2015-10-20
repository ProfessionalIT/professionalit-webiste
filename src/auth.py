import web
from google.appengine.api import users

def requires_admin(method):
    def wrapper(self, *args, **kwargs):
        user = users.get_current_user()
        if not (user and users.is_current_user_admin()):
            #raise web.seeother(users.create_login_url(web.ctx.path))
            raise web.seeother(users.create_login_url(web.ctx.path), absolute=True)
        else:
            return method(self, *args, **kwargs)
    return wrapper

def get_logged_user():
    user = users.get_current_user()
    return user

def get_logoff_url():
    url = users.create_logout_url('http://www.lindoiatc.com.br')
    return url
