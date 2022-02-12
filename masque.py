"""
masque.py - A simple Python 3 disguise module for urlopen().

Masque is designed to evade user-agent filters and tracking. It randomizes
HTTP headers of outgoing requests and adds adjustable randomized delay to
each request to avoid bans. Can be configured with external JSON files.

@name: masque.py
@author: MFritter
@date: 2022/02/11
@license: MIT
"""

from json import load
from random import choice, randrange
from time import sleep
from urllib.request import urlopen as uro, Request

# Configuration files for possible header values and settings
HEADERS = load(open('conf/headers.json', 'r'))
SETTINGS = load(open('conf/settings.json', 'r'))


def build():
    """Generate a dict of randomized HTTP headers and randomized values."""
    headers = {name: choice(HEADERS[name]) for name in SETTINGS['Mandatory']}
    for _ in range(randrange(SETTINGS['Additional Headers'])):
        key = choice(list(HEADERS.keys()-headers.keys()))
        headers[key] = choice(HEADERS[key])
    return headers


def urlopen(url, data=None, timeout=(SETTINGS['Timeout']/1000)):
    """Perform urlopen() function with random headers and time delay."""
    sleep(randrange(SETTINGS['Min Delay'], SETTINGS['Max Delay'])/1000)
    if isinstance(url, str):
        return uro(Request(url, data=data, headers=build()), timeout=timeout)
    url.headers = build()
    return uro(url, data=data, timeout=timeout)

# Config File Format
#
# settings.json contains a dict with the following objects:
#   - 'Additional Headers': Integer maximum number of headers to add
#   - 'Mandatory': List of Header names (str) that must be included
#   - 'Max Delay': Integer maximum number of milliseconds to delay a request
#   - 'Min Delay': Integer minimum number of milliseconds to delay a request
#   - 'Timeout': Integer number of milliseconds to wait for urlopen()
#
# headers.json contains a dict. The dict keys are HTTP header names, and the
# values are lists of possible values (str). An example is provided below:
# {
#   "Sec-CH-UA-Platform": [
#       "Linux",
#       "Windows",
#       "Chrome OS",
#       "macOS",
#       "Unknown"
#   ]
# }
