tool_header = """
Welcome the CBOR Handler! 
In this tool, you can:
1- Decode CBOR data
2- Request a specific value from an imported CBOR data
3- Update an imported CBOR data
sounds fun! let's start!
"""

cbor_data_request = """
Please enter a hex-encoded string that contains the CBOR data.
Ex: a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203


"""

cbor_data_hex_valid = "Hex string is correct :)"
cbor_data_hex_invalid = "looks like you you entered an invalid hex-encoded string. please try again."

cbor_data_valid = "Data is correct :)"
cbor_data_invalid = "looks like the hex_encoded string you entered is invalid cbor_data. please try again."


tool_actions = """

please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit

"""

tool_actions_invalid = """
Invalid input. please try again.
"""

tool_path_request = """
please enter the path of the required value:
How to write the path?
ex: {"key0":"example", "key1" : ["value1",45,"value3"], "key2": {"k1":true}}
root/ -> prints the whole data object
root/key0/ -> prints the value stored in key0: "example"
root/key1/ -> prints the value stored in key1: ["value1",45,"value3"]
root/key1/1/ -> prints the value of index 1 that is stored in key1: 45
root/key2/k1/ -> prints the value of k1 that is stored in key2: true


"""

tool_path_invalid = "sorry but the entered path is not valid. try 'root/' to know the keys of cbor data."

tool_update_request = """
please enter the the data to update the selected path 
[note] data will be stored as a string


"""

too_update_valid = """
invalid input, please try again
"""

tool_update_done = """
CBOR data is updated :)
"""

tool_update_invalid = """
something went wrong, please try again.
"""