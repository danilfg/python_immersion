import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
with open(storage_path, 'r') as data_file:
	data_dict = json.load(data_file)

parser = argparse.ArgumentParser()
parser.add_argument("--key", action="store")
parser.add_argument("--value", action="store")
args = parser.parse_args()
#temp_dict[args.key] = [args.value]

if args.value == None:
	print(data_dict[args.key])
else:
	if args.key not in data_dict:
		data_dict[args.key] = [args.value]
	else:
		data_dict[args.key].append(args.value)

#json.dump(data_dict, open(storage_path, 'w'))

print(data_dict)

	

