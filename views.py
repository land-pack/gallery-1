import bottle, os, json, uuid, StringIO
import Image as pilImage
from bottle import route, abort, request, HTTPError, response,\
                        post, get, delete, put, static_file, route
from models import *

image_dir = "/home/ngon2/images"
dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None

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
        orgfn, ext = os.path.splitext(f.filename)
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
            #now create a db entry for image
            im = pilImage.open(os.path.join(image_dir, fn)) 
            img_dict = {
                'width': im.size[0],
                'height': im.size[1],
                'url': fn,
                'name': orgfn + ext,
                'size': os.path.getsize(im.filename),
            }

            size = 160, 160
            im.thumbnail(size, pilImage.ANTIALIAS)
            img_dict['thumb_width'] = im.size[0]
            img_dict['thumb_height'] = im.size[1]
            thumb_output = os.path.join(image_dir, "thumb" + fn)
            im.save(thumb_output, "jpeg")

            img = Images.create(img_dict)
            session.add(img)
    session.commit()
            
    return "done"
            
@get('/json/images')
def json_all_imgs():
    d = [img.to_dict() for img in Images.get_all()]
    return json.dumps(d, default=dthandler)

@get('/json/images/<id:int>')
def json_get_img_by_id(id):
    d = Images.by_id(id).to_dict()
    return json.dumps(d, default=dthandler)


@get('/images/id/<id:int>')
def img_get_by_id(id):
    img = Images.by_id(id)
    if img:
        url = img.url
        Images.inc_view(id)
        return static_file(url, root=image_dir)
    else:
        abort(404, "image not found")

@get('/images/thumb/id/<id:int>')
def img_get_thumb_by_id(id):
    img = Images.by_id(id)
    if img:
        url = "thumb" + img.url
        return static_file(url, root=image_dir)
    else:
        abort(404, "image not found")

@get('/json/tags')
def json_all_tags():
    d = []
    for tag in Tags.get_all():
        tag_dict = tag.to_dict()

    return json.dumps(d, default=dthandler)

@get('/json/tags/<id:int>')
def get_tag_by_id(id):
    d = Tags.by_id(id).to_dict()
    return json.dumps(d, default=dthandler)

@post('/json/tags')
def json_create_tag():
    return ""



