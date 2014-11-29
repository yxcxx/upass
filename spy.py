__author__ = 'yxc'

import urllib
import cookielib
import re

from setting import URL1, URL2

VS = re.findall("dD[a-zA-Z0-9]*", urllib.urlopen(URL1).read())


class GetClassScheat():
    def __init__(self, number, password, inside=True):
        self.number = number
        self.password = password
        cookie = cookielib.CookieJar()
        url = URL1 if inside is True else URL2
        VS = re.findall("dD[a-zA-Z0-9]*", urllib.urlopen(url).read())
        params = urllib.urlencode({
            "TextBox1": self.number,
            "TextBox2": self.password,
            # "cookie": cookie,
            "_VIEWSTATE": VS,
            "dd1_js": "学生",
            "Button1": "登录"
        })

    def login(self):
        pass
