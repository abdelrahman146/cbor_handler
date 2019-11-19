import cbor2 as cbor
import binascii as encoding

import messages
import validators


# ask the user to input action number
def get_action():
    while True:
        action = input(messages.tool_actions)
        try:
            assert validators.valid_action_input(action)
        except Exception:
            print(messages.tool_actions_invalid)
            continue
        break
    return int(action)


# ask the user to provide an encoded cbor_data
def get_cbor_data():
    data = None
    while True:
        hex_str = input(messages.cbor_data_request)
        try:
            assert int(hex_str, 16)
            hex_str = encoding.unhexlify(hex_str.encode('utf-8'))
            print(messages.cbor_data_hex_valid)
        except ValueError:
            print(messages.cbor_data_hex_invalid)
            continue
        try:
            data = cbor.loads(hex_str)
            print(messages.cbor_data_valid)
        except ValueError:
            print(messages.cbor_data_invalid)
            continue
        break
    return data


# ask the user to provide the path into the data
def get_path():
    while True:
        path = input(messages.tool_path_request)
        path = path.lower()
        try:
            assert validators.valid_path(path)
        except Exception:
            print(messages.tool_path_invalid)
            continue
        return filter_path(path)


# clean and filter the provided path
def filter_path(path):
    path = path.rstrip("/")
    keys = path.split("/")
    keys = list(filter(None, keys))
    for i in range(0, len(keys)):
        try:
            keys[i] = int(keys[i])
        except ValueError:
            continue
    return keys


# takes data, transform it to cbor and then encode it
def to_hex(data):
    cbor_data = cbor.dumps(data)
    return encoding.hexlify(cbor_data).decode('utf-8')
