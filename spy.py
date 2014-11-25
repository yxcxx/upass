__author__ = 'yxc'

import urllib
import cookielib
import re

from setting import URL1, URL2


class GetClassScheat():

    def __init__(self, number, password, inside=True):
        self.number = number
        self.password = password
        cookie = cookielib.CookieJar()
        url = URL1 if inside is True else URL2
        data = urllib.urlencode({
            "number": self.number,
            "password": self.password,
            "cookie": cookie,
        })
        re.findall(r"<td>", urllib.urlopen(url, data).read())
