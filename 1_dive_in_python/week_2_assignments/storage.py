import os
import tempfile
import argparse
import json


def clear():
    with open(storage_path, "w") as f:
        f.write('')

def open_file(storage_path):
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            json_read = f.read()
            if json_read:
                json_file = json.loads(json_read)
            else:
                json_file = {}
    else:
        json_file = {}
    return json_file

temp = []
temp.extend('Liza')

def write_kv(key, value, storage_path):
    json_file = open_file(storage_path)
    if key in json_file:
        temp = []
        if isinstance(json_file[key], list):
            temp.extend(json_file[key])
        else:
            temp.append(json_file[key])
        temp.append(value)
        json_file[key] = temp
    else:
        json_file[key] = value

    with open(storage_path, 'w') as f:
        f.write(json.dumps(json_file))


def read_v(key, storage_path):
    json_file = open_file(storage_path)
    if key in json_file:
        if isinstance(json_file[key], list):
            for i in json_file[key]:
                print(i, end =" ")
        else:
            print(json_file[key])
    else:
        raise ValueError('the key is not in the list')

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', help='Clear the file')
    args = parser.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    if args.clear:
        clear()

    elif args.key and args.val:
        write_kv(args.key, args.val, storage_path)

    elif args.key:
        read_v(args.key, storage_path)

    else:
        raise ValueError('Wrong Format')
