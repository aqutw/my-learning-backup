# -*- coding: utf-8 -*-
# a Tool for LAZY

open_filename = 'my-learning-backup.txt'
tmp = """
css CSS
css3 CSS3
html HTML
html5 HTML5
rwd RWD
pwa PWA
spa SPA
reactjs ReactJS
react ReactJS
rxjs RxJS
flex flex
"""
o = {}
for v in tmp.split('\n'):
  if v:
    a = v.split(' ')
    o[a[0]] = a[1]
okeys = o.keys()
ovals = o.values()

def normal_tags(s):
  a = []
  for v in s[1:].split(' '): # Use [1:] to remove first '#'
    v2 = v.lower()
    if v2 in okeys:
      a += [o[v2]]
    else:
      a += [v.title()]
  return '#' + ' '.join(a)
  
a = []
s = ''
with open(open_filename, 'r') as f:
  s = f.read()
for v in s.splitlines():
  a += [normal_tags(v) if v.find('#')==0 else v]
s = '\n'.join(a)

with open(open_filename, 'w') as f:
  f.write(s)

print 'Done!'
