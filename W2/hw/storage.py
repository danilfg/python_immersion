import os
import tempfile
import argparse
import json

data_dict = {}

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
if os.path.isfile(storage_path):
    with open(storage_path, 'r') as data_file:
        data_dict = json.load(data_file)

parser = argparse.ArgumentParser()
parser.add_argument("--key", action="store")
parser.add_argument("--value", action="store")
args = parser.parse_args()

str = ''

if args.value == None:
    if args.key not in data_dict:
        print("")
    else:
        for i in range(len(data_dict[args.key])):
            str += data_dict[args.key][i] + ", "
        str = str[0:-2]
        print(str)
else:
	if args.key not in data_dict:
		data_dict[args.key] = [args.value]
	else:
		data_dict[args.key].append(args.value)

json.dump(data_dict, open(storage_path, 'w'))

	

