__author__ = 'yxc'

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("main.html", title="uPass")
