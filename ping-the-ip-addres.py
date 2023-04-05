#!/usr/bin/python
# -*- coding: utf-8 -*-

# @LICENSE: This code is under MIT License.
# @AUTHOR: AlirızaGövce

import socket

website = input("Enter a website to ping: ")

try:
    ip_address = socket.gethostbyname(website)
    print("IP Address of", website, "is:", ip_address)
except socket.gaierror:
    print("Could not determine IP address for", website)
