#!/usr/bin/python3
"""
module defines do_pack function that generates
a .tgz archive from the contents
of the web_static folder
"""


from fabric.api import local, run, env
from datetime import datetime
import os.path

env.hosts = ["35.175.64.13", "100.25.190.190"]

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

    archive = archive_path.split("/")[-1]
    filename = archive.split(".")[0]
    current = "/data/web_static/current"
    releases = "/data/web_static/releases/"

    if put(archive_path, "/tmp/{}".format(archive)).failed is True:
        return False
    if run("rm -rf {}{}/".
           format(releases, filename)).failed is True:
        return False
    if run("mkdir -p {}{}/".
           format(releases, filename)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C {}{}/".
           format(archive, releases, filename)).failed is True:
        return False
    if run("rm /tmp/{}".format(archive)).failed is True:
        return False
    if run("mv {}{}/web_static/* {}{}/".
           format(releases, filename, releases, filename)).failed is True:
        return False
    if run("rm -rf {}{}/web_static".
           format(releases, filename)).failed is True:
        return False
    if run("rm -rf {}".format(current)).failed is True:
        return False
    if run("ln -s {}{}/ {}".
           format(releases, filename, current)).failed is True:
        return False
    return True


def deploy():
    """creates and distributes an archive to web servers"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)