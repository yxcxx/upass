__author__ = 'yxc'

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define, options

from url import HANDLER
from setting import setting

define("port", default=8000, help="app run in this port")


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, HANDLER, **setting)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
