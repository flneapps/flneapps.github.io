#!/usr/bin/env python
#-*- coding: utf-8 -*-

import commands
from time import strftime


resolvers = {
    'Google Public': '8.8.8.8',
    'KT Olleh': '168.126.63.1',
    'KT Olleh Mobile': '211.246.100.20',
    'SK Broadband': '210.220.163.82',
    'SK Telecom': '211.234.229.23',
    'LG Dacom Corporation' : '164.124.101.2',
    'LG U+' : '164.124.107.9'
  }

sep = "\n%s\n" % ("-" * 72)

summaries = []
raws = []

def try_until_answer(addr):
  left = 5
  while left > 0:
    left -= 1
    res = commands.getoutput("dig www.flneapps.co.kr @%s" % addr)
    if res.find("ANSWER SECTION") != -1:
      return res

  return res

for name, addr in resolvers.iteritems():
  res = try_until_answer(addr)

  summary = "%s (%s): " % (name, addr)
  if res.find("127.0.0.1") != -1:
    summary += "BLOCKED!"
  else:
    summary += "OK"

  summaries.append(summary)
  raws.append(summary + "\n" + res)


filename = "./results/%s.txt" % strftime('%y%m%d_%H%M')

f = open(filename, 'w')
f.write('\n'.join(
  ["www.flneapps.co.kr 차단 여부 조회 결과",
   "\n[요약]\n",
   "\n".join(summaries),
   "\n\n[전체 로그]\n",
   sep.join(raws)]
  ))
f.close()

print "Done, the result is saved in %s." % filename
