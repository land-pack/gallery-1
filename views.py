import bottle, os, json, uuid
from bottle import route, abort, request, HTTPError, HTTPResponse, post, get, delete, put
from models import *

image_dir = "/home/ngon2/images"

@get('/upload')
def upload_get():
    html = '''
<!DOCTYPE html>
<html>
<head>
</head>

<body>
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="data" multiple="multiple"/>
    <input type="submit" />
</form>
</body>
</html>

'''
    return html

@post('/upload')
def upload():
    files = request.files.getlist('data')
    for f in files:
        ext = os.path.splitext(f.filename)[1]
        ext = ext.lower()
        if ext == ".jpeg" or ext == ".jpg" or ext == ".png":
            fn = str(uuid.uuid4()) + ext
            chunk = None
            fout = file (os.path.join(image_dir, fn), 'wb')
            while (1):
                chunk = f.file.read(100000)
                if not chunk:
                    break;
                fout.write(chunk)
            fout.close()
    return "done"
            
            
        
