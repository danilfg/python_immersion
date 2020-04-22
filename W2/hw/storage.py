import os
import tempfile
import argparse
import json
from pathlib import Path

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
with open(storage_path, 'r+') as data_file:
	data_dict = data_file.read()

parser = argparse.ArgumentParser()
parser.add_argument("--key", action="store")
parser.add_argument("--value", action="store")
args = parser.parse_args()
temp_dict = data_dict
temp_dict[args.key] = [args.value]



#json.dump(temp_dict, open(storage_path, 'w'))

print(temp_dict)

	

