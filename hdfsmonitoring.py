#!/usr/bin/env python
import socket
import smtplib
import os
import subprocess
import sys
from email.mime.text import MIMEText


def get_lock(process_name):
   global lock_socket
   lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
   try:
       lock_socket.bind('\0' + process_name)
       print 'Lock Monitoring hdfs'
   except socket.error:
       sendalert("service in hold")
       print 'Lock exists'
       sys.exit()


def sendalert(pesan):
      s = smtplib.SMTP('alamat ip smtp')
      msg = MIMEText(""" %s """ % pesan)
      sender = 'alamat pengirim'
      recipients = ['alamat penerima']
      msg['Subject'] = "Monitoring Disk Usage di HDFS "
      msg['From'] = sender
      msg['To'] = ", ".join(recipients)
      s.sendmail(sender, recipients, msg.as_string())


def proses():
     get_lock("monitoring_diskfragment_usage")
     cmd = '''/usr/bin/hadoop fs -df / | /usr/bin/awk {'print $5'}  '''
     listen = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
     string = listen.stdout.read()
     num = int(str.replace(string,"%","")) 
     cmd2 = '''hadoop fs -du -s -h '/*'  '''
     listen = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
     string2 = listen.stdout.read()
     if num >= 80:
        sendalert("Storage di HDFS sudah mencapai "+str(num)+"%\n\n"+str(string2))
     else:
        pass
        sys.exit()



if __name__ == "__main__":
     proses()
