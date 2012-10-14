import bottle
from bottle import route, abort, request, HTTPError, HTTPResponse, post, get, delete, put
import json
from models import *

@get('/upload')
def upload_get():
    html = '''
<!DOCTYPE html>
<html>
<head>
</head>

<body>
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="text" name="name" />
    <input type="file" name="data" />
    <input type="submit" />
</form>
</body>
</html>

'''
    return html

@post('/upload')
def upload():
    data = request.files.data
    if data and data.file:
        raw = data.file.read() # This is dangerous for big files
        filename = data.filename
        return "Hello You uploaded %s (%d bytes)." % (filename, len(raw))
    return "You missed a field."
