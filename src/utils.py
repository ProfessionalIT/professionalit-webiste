#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

def remove_accents(c):
    if c in u'áàãâ': return 'a'
    elif c in u'é': return 'e'
    elif c in u'í': return 'i'
    elif c in u'óõô': return 'o'
    elif c in u'ú': return 'u'
    elif c in u'ç': return 'c'
    else: return c

def markdown(text):
    from lib.markdown import markdown
    return markdown(text)

def timestamp(d=None):
    '''returns a string representing a given datetime up to the microsecond.
    Couldnt find a way to use strftime up to that precision'''
    import datetime
    date = d or datetime.datetime.now()
    microseconds = date.isoformat().split('.')[-1]
    return ''.join([datetime.datetime.strftime(date, '%Y%m%d%H%M%S'), microseconds])

def slugify(s):
    """Convert some string to a url-friendly name."""
    s = ''.join([remove_accents(x) for x in s.lower()])
    return re.sub(r'[^a-zA-Z0-9_]+', '-', s.replace("'", '')).lower().strip('-')

def versionate(s):
    """
    Assumes s is a slug-type string.
    Returns another slug-type string with a number at the the end.
    Useful when you want unique slugs that may have been hashed to the same string.
    """
    words = s.split("-")
    if len(words) > 1:
        try:
            # Check if the last element is a number. If no exception, it is.
            # We'll substitute the number on the slug
            num = int(words[-1])
            words[-1] = str(num+1)
        except ValueError:
            #Not a number. We'll append the number 1 to create a new version.
            words.append('1')
        
    return '-'.join(words)


def save_uploaded_file(f, **kw):
    import datetime
    
    name = kw.pop('name', None)      
    folder = kw.pop('folder', './')

    uploaded_filename = str(f)
    extension = ('.' in uploaded_filename and uploaded_filename.split('.')[-1]) or ''
    
    filename = str(name) if name is not None else '.'.join([timestamp(), extension])
    
    destination = open(os.path.join(folder, filename), 'w')
    for chunk in f.chunks():
        destination.write(chunk)
        destination.close()
   
    return filename

def parseBoolString(theString):
    return theString[0].upper()=='T' 

def break_string(theString):
    has_value=theString != '' and theString != 'NULL' and theString != None and theString != 'None'
    if has_value:
        try:
            return theString + '\n'
        except UnicodeEncodeError:
            logging.debug("UnicodeEncodeError")
            return theString.decode('utf-8')
        except:
            logging.debug("Deu pau no Utils:", sys.exc_info()[0])
            return theString.encode('utf-8')
    else:
        return '\n'

