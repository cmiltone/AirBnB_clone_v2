#!/usr/bin/python3
"""
module defines do_pack function that generates
a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os.path

def do_pack():
    """generates
    a .tgz archive from the contents
    of the web_static folder
    """
    t = datetime.utcnow()
    y = t.year
    m = t.month
    d = t.day
    h = t.hour
    m = t.minute
    s = t.second
    stamp = "{}{}{}{}{}{}".format(y, m, d, h, m, s)
    filepath = "versions/web_static_{}".format(stamp)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(filepath)).failed is True:
        return None
    return filepath
