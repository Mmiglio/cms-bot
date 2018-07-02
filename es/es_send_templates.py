#!/usr/bin/python
from os.path import dirname, basename, abspath, join, exists
import sys, json

cmsbot_dir=None
if __file__: cmsbot_dir=dirname(dirname(abspath(__file__)))
else: cmsbot_dir=dirname(dirname(abspath(argv[0])))
sys.path.insert(0,cmsbot_dir)

from es_utils import send_template

for tmpl in sys.argv[1:]:
  tmplfile = join(cmsbot_dir,'es', 'templates',tmpl+'.json')
  if not exists (tmplfile):
    print "ERROR: No such file: ",tmplfile
    sys.exit(1)
  payload = json.load(open(tmplfile))
  if not send_template(tmpl, payload=json.dumps(payload)): sys.exit(1)

