#!/usr/bin/python3

import os
import datetime

def consolidate ():
  
  #Reading the certificate, bundle and the private key
  with open ("/etc/apache2/ssl/sslcertificate.crt","r") as f1:
    cert = f1.read()
  with open ("/etc/apache2/ssl/gd_bundle-g4-g5.crt", "r") as f2:
    bundle = f2.read()
  with open ("/etc/apache/ssl/theprivatekey.key") as f3:
    pk=f3.read()
    
  #Creating the Consolidation and Backup Folder (if not existing already)
  consolidationpath="/etc/haproxy/consolidation"
  if not os.path.exists(consolidationpath):
    os.mkdir(consolidationpath)
  
  backupath="/home/backup"
  if not os.path.exists(backuppath):
    os.mkdir(backupath)
