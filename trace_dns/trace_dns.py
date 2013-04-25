#!/usr/bin/env python
#-*- coding: utf-8 -*-

import commands


resolvers = {
    'Google Public': '8.8.8.8',
    'KT olleh': '168.126.63.1',
    'SK Broadband': '210.220.163.82',
    'SK Telecom': '211.234.229.23',
    'LG Dacom Corporation' : '164.124.101.2',
    'LG U+' : '164.124.107.9'
  }

print "www.flneapps.co.kr DNS 조회 결과"

for name, addr in resolvers.iteritems():
  print "-" * 72
  print "%s (%s): " % (name, addr)
  print commands.getoutput("dig www.flneapps.co.kr @%s +nocomments" % addr)
