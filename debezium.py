import requests
import json
from os import environ
import sys



def open_file(config_file):
    with open(config_file, 'r') as file:
        data = file.read()
        data = json.loads(data)


    for key, value in data['config'].items():
        if '$' in value:
            value = value.replace('$', '')
            data['config'][key] = environ[value]

    return data



def add_config(config_file):
    data = open_file(config_file)
    print(f'Sending config file "{config_file}" to add a connection.')
    print(data)


def delete_config(connector):
    response = requests.delete(
        f'http://redpanda.hostinger.io:8083/connectors/{connector}',
    )

    response.raise_for_status()

    print(response.text)


def update_config(config_file):
    print(f'Sending config file "{config_file}" to update a connection.')
    data = open_file(config_file)

    print(data)




if __name__ == "__main__":
    type = sys.argv[1]
    config_files = sys.argv[2].split(' ')

    if config_files == ['']:
        print(f'No config files to {type} a connection.')
    else:

        if type == 'add':
            for file in config_files:
                add_config(file)
        elif type == 'update':
            for file in config_files:
                update_config(file)



