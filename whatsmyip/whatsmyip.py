#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""Script that do a query to a server to renseign internal ip and hostname
"""
import socket
import fcntl
import struct
import urllib2

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

server_script_url = 'http://plebweb.fr/cours-iot/whatsmyip.php'

hostname = socket.gethostname()
internal_ip = get_ip_address('wlan0')

request_url = server_script_url + '?internal_ip=' + internal_ip + '&hostname=' + hostname

urllib2.urlopen(request_url).read()

