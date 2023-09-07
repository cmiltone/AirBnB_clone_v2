#!/usr/bin/python3
"""
module defines do_pack function that generates
a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import local, run
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
    filepath = "versions/web_static_{}.tgz".format(stamp)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(filepath)).failed is True:
        return None
    return filepath


def do_deploy(archive_path):
    """
    distributes an archive to web servers
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
