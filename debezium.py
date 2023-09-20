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



def send_config(config_file):
    data = open_file(config_file)

    print(data)
    # response = requests.post(
    #     'http://redpanda.hostinger.io:8083/connectors',
    #     json=data,
    #     headers={'Accept': 'application/json', 'Content-Type': 'application/json'}
    # )
    #
    # response.raise_for_status()
    #
    # print(response.text)


def delete_config(connector):
    response = requests.delete(
        f'http://redpanda.hostinger.io:8083/connectors/{connector}',
    )

    response.raise_for_status()

    print(response.text)


def update_config(config_file):
    data = open_file(config_file)

    print(data)

    # response = requests.put(
    #     f'http://redpanda.hostinger.io:8083/connectors/{data["name"]}/config',
    #     json=data['config'],
    #     headers={'Accept': 'application/json', 'Content-Type': 'application/json'}
    # )
    #
    # response.raise_for_status()
    #
    # print(response.text)


if __name__ == "__main__":
    type = int(sys.argv[1])
    config_files = sys.argv[2].split(' ')

    if type == 0:
        for file in config_files:
            send_config(file)
    elif type == 1:
        for file in config_files:
            update_config(file)



