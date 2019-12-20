# # master_valve.py
# # apt-get install python-paste
# # apt-get install python-PasteDeploy
#
# from paste import httpserver
# from paste.deploy import loadapp
#
# if __name__ == '__main__':
#     httpserver.serve(loadapp('config:test-paster.ini', relative_to='.'),
#                      host='127.0.0.1', port=8000)


from wsgiref.simple_server import make_server
from paste import httpserver
from paste.deploy import loadapp
import os

if __name__ == '__main__':
    configfile = 'configure.ini'
    appname = 'main'
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)

    # httpserver.serve(loadapp('config:configure.ini', relative_to = '.'), host = '127.0.0.1', port=8000)

    server = make_server('localhost', 8000, wsgi_app)
    server.serve_forever()
