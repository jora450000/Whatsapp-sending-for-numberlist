#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import system
from random import randint
from time import sleep
import ipgetter


txt=["Only today you have big chance to win ..... +7-232323-28503-44 " ,
"Only  t o d a y   you have big chance to win ..... +7 232323 28 50 344",
"Only today YOU!!!  have big chance to win ..... +7 232 323 285 0344",
"Today  have big chance to win ..... +7 232323 285 034 4",
"You have big chance to win ..... +7 232323 28 50344",
"You have chance to win ..... +7 232323 2850344",
"Do you want to win? Call to  +7 232 323 285 0344")




fname = "/var/moni/numbers.txt"

with open(fname) as f:
  numbers = f.readlines()
  for number in numbers:
      print  number
      if number[-1] == '\n':
            number = number[:-1]

      IP = ipgetter.myip()
      while (IP  == '1.2.3.4'):  # replace with your outside IP
	  system("killall  openvpn")
	  sleep(2)
          system("openvpn /var/moni/" + str(randint(1,7))  +  ".ovpn &  >> ip.log")
          sleep(10)
	  IP = ipgetter.myip()    
      print("My IP: " + IP)      
      s="/var/moni/yowsup-cli demos -c config"+ str(randint(1,3))  +  "  --unmoxie  -s  "+ number + "  \"" +  txt[randint(0,7)] + "\" "
      print s
      system(s)
#      IP = ipgetter.myip()
      sleep(randint(20,30))
      system("killall openvpn")
      sleep(randint(10,50))

