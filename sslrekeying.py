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
 
    #Checking if the consolidated.pem doesn't already exist and creating it
    cons="/etc/haproxy/consolidation/consolidated.pem"
    if os.path.exists(cons):
      counter=1
      f,ext=os.path.splitext(cons)
      newcons=f+str(datetime.date.today())+ext
      with open (newcons,'w')as f4:
        f4.write(cert+bundle+pk)
    else:
      counter=2
      with open (cons,'w') as f4:
        f4.write(cert+bundle+pk)
    
    #Reading the haproxy.cfg file
    with open ("/etc/haproxy/haproxy.cfg","r") as f5:
      haproxycfg=f5.read()
  
    #Checking if haproxy.cfg exists in the backup folder otherwise creating a copy
    haproxypath = "/home/backup/haproxy.cfg"
    if os.path.exists(haproxypath):
      f,ext=os.path.splitext(haproxypath)
      newhaproxypath=f+str(datetime.date.today())+ext
      with open (newhaproxypath,'w') as f6:
        f6.werite(haproxycfg)
    else:
      with open (haproxypath,'w') as f6:
        f6.write(haproxycfg)
    
    #Editing the haproxy.cfg file with the new path accordingly
    if counter==1:
      haproxycfg=haproxycfg.replace("/etc/haproxy/certs/newcert.pem",newcons)
    elif counter==2:
      haproxycfg=haproxycfg.replace("/etc/hproxy/certs/newcert.pem",cons)
    with open("/etc/haproxy/haproxy.cfg",'w') as f7:
      f7.write(haproxycfg)
  
    #Restarting the haproxy services
    os.system("sudo /etc/init.d/haproxy restart")

  
def main():
    consolidate()
    
  
if __name__=='__main__':
    main()
