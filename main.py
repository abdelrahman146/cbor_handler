import messages
import helpers


# a recursive function to extract a specific value from data
def get_value(list, cbor_data):
    if len(list) == 1:
        try:
            return cbor_data[list[0]]
        except Exception:
            return
    for key in cbor_data:
        try:
            if key == list[0]:
                cbor_data = cbor_data[key]
                break
        except Exception:
            return
    list.pop(0)
    return get_value(list, cbor_data)


# a function to loop through data to change a specific value
def change_value(path, cbor_data, new_data):
    itr_data = cbor_data
    try:
        for i in range(0, len(path)):
            changed = False
            for key in itr_data:
                if key == path[i] and i == len(path) - 1:
                    itr_data[key] = new_data
                    changed = True
                    break
                elif key == path[i]:
                    itr_data = itr_data[key]
                    changed = True
                    break
            if not changed:
                return
    except Exception:
        return
    return cbor_data


# the print option function, takes path into the data and returns the correspondent value
def print_value(cbor_data):
    path = helpers.get_path()
    if len(path) == 1:
        return cbor_data
    else:
        path.pop(0)
        return get_value(path, cbor_data)


# the update option function, takes path into the data a string update the data and returns a new hex string
def update_value(cbor_data):
    path = helpers.get_path()
    new_data = input(messages.tool_update_request)
    if len(path) == 1:
        return new_data
    else:
        path.pop(0)
        return change_value(path, cbor_data, new_data)


# the starting point, gets the user required action and call the correspondent function
def start_tool():
    while True:
        action = helpers.get_action()
        if action == 0:
            break
        cbor_data = helpers.get_cbor_data()
        if action == 1:
            result = print_value(cbor_data)
            if not result:
                print(messages.tool_path_invalid)
            else:
                print(result)
        if action == 2:
            result = update_value(cbor_data)
            if not result:
                print(messages.tool_path_invalid)
            else:
                print(messages.tool_update_done)
                print(helpers.to_hex(result))

