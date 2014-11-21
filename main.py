__author__ = 'yxc'

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define, options

define("port", default=8000, help="app run in this port")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]

        settings = dict(
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.write("Hello world")

    def post(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
