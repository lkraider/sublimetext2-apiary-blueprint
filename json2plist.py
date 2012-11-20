import plistlib
import json
import sys

filename = sys.argv[1]

d = json.load(open(filename))
plistlib.writePlist(d, '%s.tmLanguage' % filename.partition('.json')[0])
