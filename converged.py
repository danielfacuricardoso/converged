#!/bin/usr/env python
#!coding: utf-8
import os

host = "google.com"
dados = os.system("curl " + host)
print dados

if dados == 0:
        os.system("echo 1 > /home/filos/arquivo") 
else:
        os.system("echo 2 > /home/filos/arquivo") 
