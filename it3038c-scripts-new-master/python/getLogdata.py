import os
filename = "/var/log/secure"

with open(filename) as f:
  lines = set(f.read() .splitline())
  for line in lines:
  if "root" in line:
  print(line)