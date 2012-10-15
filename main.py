from bottle import route, run, template
from models import *
from views import *
from static import *

run(host='192.168.15.181', port=8080, reloader=True)
