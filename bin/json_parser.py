import json, sys
from pprint import pprint

if len(sys.argv) < 2:
    print "Usage: python json_parser.py [json_file]"
    exit(1)

json_in = sys.argv[1]

with open(json_in) as data_file:
    data = json.load(data_file)

for key in data:
    print key

print "========== StateModels ==============="
data['StateModels'].append({'StateId':'SpotifyPlay'})

print json.dumps(data['StateModels'], sort_keys=True, indent=4, separators=(',', ': '))

# pprint(data)