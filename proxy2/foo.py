#!/usr/bin/python3

from tld import get_fld

fldList = []
domList = open("domain2.txt").read().splitlines()
for dom in domList:
  fldList.append(get_fld(dom, fix_protocol=True))

print("\n".join(sorted(set(fldList)))
