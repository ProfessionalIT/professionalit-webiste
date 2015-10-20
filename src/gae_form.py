# -*- coding: utf-8 -*-
"""
HTML forms
(part of web.py)
"""
from web.form import *
import logging
from google.appengine.ext import db

def gae_attrget(obj, attr, value=None):
    if isinstance(obj,db.Model):
        try:
            if attr == 'key':
                return obj.key()
            gae_attribute = getattr(obj,attr)
            if isinstance(gae_attribute,db.Model):
                id_reference = gae_attribute.key().id()
                #logging.debug(' ############# : ' + str(id_reference))
                return id_reference
            else:
                #logging.debug(' ************ : ' + str(gae_attribute))
                return gae_attribute
        except Exception, ex:
            logging.debug(ex)
    else:
        if hasattr(obj, 'has_key') and obj.has_key(attr): return obj[attr]
        if hasattr(obj, attr): return getattr(obj, attr)
    return value


class GAEForm(Form):

    def validates(self, source=None, _validate=True, **kw):
        source = source or kw or web.input()
        out = True
        for i in self.inputs:
            v = gae_attrget(source, i.name)
            if _validate:
                out = i.validate(v) and out
            else:
                i.value = v
        if _validate:
            out = out and self._validate(source)
            self.valid = out
        return out
