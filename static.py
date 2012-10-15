from bottle import route, abort, request, HTTPError, HTTPResponse,\
                        post, get, delete, put, static_file, route

image_dir = "/home/ngon2/images/"
static_dir = "/home/ngon2/photo/static/"

@route('/images/name/<fn:path>')
def get_images(fn):
    return static_file(fn, root=image_dir)

@route('/html/<fn:path>')
def get_html(fn):
    return static_file(fn, root=static_dir + 'html/')

@route('/css/<fn:path>')
def get_css(fn):
    return static_file(fn, root=static_dir + 'css/')

@route('/js/<fn:path>')
def get_js(fn):
    return static_file(fn, root=static_dir + 'js/')




