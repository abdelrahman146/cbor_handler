# Simple CBOR Handler

A simple CBOR handler that does two things:

1. **Read data from a CBOR data:**

   The tool allows the user to input CBOR data as a hex-encoded string along with a path into the data represented by a string

   The tool will then return the decoded data contained at the path. 

2. **Change values in a CBOR data:**

   The tool allows the user to input CBOR data as a hex-encoded string, a path into the data as a string, and a third piece of arbitrary data.

   The tool will then return new bit of CBOR hex-encoded data that is the same as the CBOR data that was passed in, but with the data at the input path replaced with the arbitrary input data.


## Programming language
- the tool was built and tested on python 3.8

## How To open the tool

1. Git clone: `git clone https://github.com/abdelrahman146/cbor_handler`
2. go the dist directory: `cd cbor_handler/dist/main`
3. run the executable file: `main.exe`

## How to use the tool
The cbor handler is a CLI tool.

1. The tool will ask you to choose which option you would like to try

example: 

```
Welcome the CBOR Handler! 
In this tool, you can:
1- Decode CBOR data
2- Request a specific value from an imported CBOR data
3- Update an imported CBOR data
sounds fun! let's start!

please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit
```
the user should pick a number from 0 to 2

2. The tool will then ask the user to provide the cbor hex-encoded data:

example:

```
Please enter a hex-encoded string that contains the CBOR data.
Ex: a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203


```
3. The tool will then ask the user to provide a path into the data (what data to decode or to alter)

example:

```
please enter the path of the required value:
How to write the path?
ex: {"key0":"example", "key1" : ["value1",45,"value3"], "key2": {"k1":true}}
root/ -> prints the whole data object
root/key0/ -> prints the value stored in key0: "example"
root/key1/ -> prints the value stored in key1: ["value1",45,"value3"]
root/key1/1/ -> prints the value of index 1 that is stored in key1: 45
root/key2/k1/ -> prints the value of k1 that is stored in key2: true

```

4. if the user chose option 2 (update data), the tool will ask the user to enter the new data

**important note:** the new data will only be stored as a string

example: 

```
please enter the the data to update the selected path 
[note] data will be stored as a string

```

5. the tool will return the result of each option:


### Examples

#### Case 1: Data decoding

```
Welcome the CBOR Handler! 
In this tool, you can:
1- Decode CBOR data
2- Request a specific value from an imported CBOR data
3- Update an imported CBOR data
sounds fun! let's start!



please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit

1

Please enter a hex-encoded string that contains the CBOR data.
Ex: a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203


a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203
Hex string is correct :)
Data is correct :)

please enter the path of the required value:
How to write the path?
ex: {"key0":"example", "key1" : ["value1",45,"value3"], "key2": {"k1":true}}
root/ -> prints the whole data object
root/key0/ -> prints the value stored in key0: "example"
root/key1/ -> prints the value stored in key1: ["value1",45,"value3"]
root/key1/1/ -> prints the value of index 1 that is stored in key1: 45
root/key2/k1/ -> prints the value of k1 that is stored in key2: true


root/
{'hello': 'world', 'obj': {1: 'first', 2: 'second', 3: [1, 2, 3]}}


please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit

1

Please enter a hex-encoded string that contains the CBOR data.
Ex: a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203


a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203
Hex string is correct :)
Data is correct :)

please enter the path of the required value:
How to write the path?
ex: {"key0":"example", "key1" : ["value1",45,"value3"], "key2": {"k1":true}}
root/ -> prints the whole data object
root/key0/ -> prints the value stored in key0: "example"
root/key1/ -> prints the value stored in key1: ["value1",45,"value3"]
root/key1/1/ -> prints the value of index 1 that is stored in key1: 45
root/key2/k1/ -> prints the value of k1 that is stored in key2: true


root/hello
world


please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit

0
```

#### Case2: Update CBOR data

```
Welcome the CBOR Handler! 
In this tool, you can:
1- Decode CBOR data
2- Request a specific value from an imported CBOR data
3- Update an imported CBOR data
sounds fun! let's start!



please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit

2

Please enter a hex-encoded string that contains the CBOR data.
Ex: a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203


a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203
Hex string is correct :)
Data is correct :)

please enter the path of the required value:
How to write the path?
ex: {"key0":"example", "key1" : ["value1",45,"value3"], "key2": {"k1":true}}
root/ -> prints the whole data object
root/key0/ -> prints the value stored in key0: "example"
root/key1/ -> prints the value stored in key1: ["value1",45,"value3"]
root/key1/1/ -> prints the value of index 1 that is stored in key1: 45
root/key2/k1/ -> prints the value of k1 that is stored in key2: true


root/obj/3

please enter the the data to update the selected path 
[note] data will be stored as a string


Great

CBOR data is updated :)

a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e6403654772656174


please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit

1

Please enter a hex-encoded string that contains the CBOR data.
Ex: a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e640383010203


a26568656c6c6f65776f726c64636f626aa30165666972737402667365636f6e6403654772656174
Hex string is correct :)
Data is correct :)

please enter the path of the required value:
How to write the path?
ex: {"key0":"example", "key1" : ["value1",45,"value3"], "key2": {"k1":true}}
root/ -> prints the whole data object
root/key0/ -> prints the value stored in key0: "example"
root/key1/ -> prints the value stored in key1: ["value1",45,"value3"]
root/key1/1/ -> prints the value of index 1 that is stored in key1: 45
root/key2/k1/ -> prints the value of k1 that is stored in key2: true


root/
{'hello': 'world', 'obj': {1: 'first', 2: 'second', 3: 'Great'}}


please select one of the following actions by writing the action number (ex: 1): 
1- Print value contained in a specific path
2- Update value contained in a specific path
0- exit

0
```

### Code Description

- `main.py`: holds the main functionalities of the tool
- `helpers.py`: holds some supporting functions such as input_filerting and cbor encoding.
- `validators.py`: holds some validator functions to validate the inputs.
- `messages.py`: holds all the information, error, and update text messsages.