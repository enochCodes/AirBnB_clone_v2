#!/usr/bin/python3
"""
1-pack_web_static module
This script generates a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates .tgz file
    from the content of the web_static"""
    now = datetime.utcnow()
    year = now.year
    month = now.month if now.month > 9 else f"0{now.month}"
    day = now.day if now.day > 9 else f"0{now.day}"
    hour = now.hour if now.hour > 9 else f"0{now.hour}"
    minute = now.minute if now.minute > 9 else f"0{now.minute}"
    second = now.second if now.second > 9 else f"0{now.second}"
    path = f"versions/web_static_{year}{month}{day}{hour}{minute}{second}.tgz"
    recource = "/data/web_static/"
    if local("mkdir -p versions").failed:
        return None
    if local(f"tar -czvf {path} {resource}").failed:
        return None
    return path
